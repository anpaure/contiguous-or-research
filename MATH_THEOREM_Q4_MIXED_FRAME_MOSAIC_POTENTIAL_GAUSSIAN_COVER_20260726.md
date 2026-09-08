# The `Q_4` mixed-frame mosaic: complete potential shadows but a Gaussian capacity cut

Date: 2026-07-26

## 0. Outcome

Assume that `m` is even and partition `[2m]` into `b=m/2` labelled
four-sets.  On one four-set write

\[
 E_1=\{12,13\},\qquad
 E_2=\{14,24\},\qquad
 E_3=\{23,34\}.                                      \tag{0.1}
\]

These three Johnson edges partition the six two-sets.  Apply this local
partition independently in every four-block, freezing local subsets of
sizes different from two.  The resulting product cells are physical
orientation cubes and partition the entire middle layer exactly.  Their
local pair frames vary with the owner; already in one block their frame
union is connected.

Call a target *potentially lower realizable*
at depth `q` if it is the intersection of a return-free length-`q` path
inside one product cell, and define potential upper realizability dually.
For every `H=o(m)`, there is an absolute `c>0` such that

\[
 \boxed{
 \sum_{q=1}^{H}\left(B_q^-+B_q^+\right)
 \le 2H e^{-cm}\binom{2m}{m}=o(W),}                  \tag{0.2}
\]

where `B_q^-/B_q^+` are the numbers of targets which are not potentially
lower/upper realizable.  In fact, a typical target has `Theta(m)` usable
local blocks, while only `q=o(m)` are needed.

This does **not** remove the Gaussian Hall obstruction.  A source owner
can supply only one depth-`q` occurrence.  For a target block type with
`g` good singleton blocks and `u` local two-set blocks, the exact ratio of
compatible source owners to targets is

\[
 \boxed{
 R_q(g,u)=\frac{2^q\binom gq}{\binom{u+q}q}.}          \tag{0.3}
\]

At `q=floor(A sqrt(m))`, on a positive-density family of typical target
types,

\[
                         R_q(g,u)\longrightarrow e^{-6A^2}<1. \tag{0.4}
\]

Consequently every choice of one cycle factor in every product cell has a
linear lower-target deficit at that depth; by complementation the same is
true on the upper side.  Thus the theorem draws a sharp distinction:

* target-by-target reachability is exponentially complete;
* simultaneous one-occurrence capacity still fails linearly.

The theorem is deliberately a **potential** coverage theorem.  It does
not choose one cycle factor in every product cube.  Formula (0.3) proves
that this distinction is essential: the frozen four-block profile is a
capacity obstruction even though it is not a support obstruction.  A
positive hierarchical mosaic must move owners between block profiles, not
merely choose better paths inside the fixed product cells.

## 1. The exact mixed-frame owner partition

Let the four-blocks be

\[
                         B_1,\ldots,B_b,
 \qquad |B_i|=4.                                    \tag{1.1}
\]

In one block, every local two-set belongs to exactly one edge in (0.1).
Group the two endpoints of that edge into a `Q_1` cell.  Every local set
of size `0,1,3,4` is a singleton cell.  Taking Cartesian products over the
blocks partitions `2^[2m]`; restricting to total rank `m` partitions
`binom([2m],m)`.

If a global cell has `s` blocks whose local rank is two, it is a physical
`Q_s`: its `s` active directions are the coordinate swaps prescribed by
the corresponding edges in (0.1), and all other local data are frozen.
Different global cells may use incompatible coordinate pairs.  Thus this
is an exact mixed-frame packet mosaic rather than one status partition of
one perfect matching.

The lower intersections and upper unions of the local edges are

\[
 \begin{array}{c|c|c}
  &\text{intersection}&\text{union}\\ \hline
 E_1&1&123\\
 E_2&4&124\\
 E_3&3&234.
 \end{array}                                           \tag{1.2}
\]

Hence the good lower singletons are

\[
                         {\cal G}^- =\{1,3,4\},       \tag{1.3}
\]

and the good upper triples are

\[
                         {\cal G}^+ =\{123,124,234\}.
                                                               \tag{1.4}
\]

They are exchanged by complementation in the block.

## 2. Potential path realization

### Lemma 2.1 (lower realization criterion)

Let `T` be an `(m-q)`-set.  If at least `q` blocks have local trace
`T cap B_i` in `G^-`, then `T` is the intersection of a return-free
length-`q` path inside one product cell.

#### Proof

Choose `q` such blocks.  In each chosen block, (1.2) gives one local edge
whose two endpoints have intersection `T cap B_i`.  Choose either endpoint
as the initial local two-set.  In every unchosen block use the local set
`T cap B_i` itself.

The initial global set has size `|T|+q=m`.  Toggle the chosen local edges
once each, in any order.  The toggles use disjoint four-blocks, so the path
is return-free.  In an unchosen block the local intersection is unchanged;
in a chosen block it is the displayed good singleton.  The global
intersection is exactly `T`.  All states lie in the same product cell.
\(\square\)

### Lemma 2.2 (upper realization criterion)

Let `U` be an `(m+q)`-set.  If at least `q` blocks have local trace
`U cap B_i` in `G^+`, then `U` is the union of a return-free length-`q`
path inside one product cell.

#### Proof

Use the local edges whose unions are the chosen good triples.  The initial
set is obtained from `U` by replacing each chosen triple by either
two-set endpoint of its edge, and therefore has size `m`.  Toggle the
`q` disjoint local edges.  The union in every chosen block is the required
triple, and all other blocks are fixed.  \(\square\)

Thus only a lower tail for the number of good singleton/triple blocks can
create a potential hole.

## 3. Exact generating function

For a set `T`, let `G^-(T)` be the number of blocks in which its local
trace is one of the three good singletons.  The bivariate one-block
polynomial is

\[
 f(x,y)=1+x(1+3y)+6x^2+4x^3+x^4
       =(1+x)^4-3x(1-y).                              \tag{3.1}
\]

Consequently, for `k=m-q`,

\[
 \sum_{T\in\binom{[2m]}k} y^{G^-(T)}
 =[x^k]f(x,y)^b.                                      \tag{3.2}
\]

At `y=1`, this is `[x^k](1+x)^(4b)=binom(2m,k)`, as it must be.

Upper triples have the same generating function by blockwise
complementation.

## 4. Uniform exponential lower-tail bound

Fix `theta=1` and put

\[
                         t={k\over4b-k}.
                                                               \tag{4.1}
\]

The `k`-th term of `(1+t)^(4b)` is a mode: the ratios to the preceding
and following terms are respectively greater and less than one.  Since
there are `4b+1` terms,

\[
 \binom{4b}{k}t^k\ge{(1+t)^{4b}\over4b+1}.           \tag{4.2}
\]

All coefficients of `f(x,e^{-1})^b` are nonnegative, so

\[
 [x^k]f(x,e^{-1})^b
 \le {f(t,e^{-1})^b\over t^k}.                       \tag{4.3}
\]

Divide (4.3) by (4.2).  For a uniform `k`-set,

\[
 \mathbb E e^{-G^-(T)}
 \le(4b+1)
 \left(1-{3t(1-e^{-1})\over(1+t)^4}\right)^b.       \tag{4.4}
\]

Uniformly for `1<=q<=H=o(m)`, one has `k/(4b)=1/2-o(1)` and
`t=1-o(1)`.  Hence the fraction subtracted in (4.4) is bounded below by
an absolute positive constant for all large `m`.  There is therefore
`c_0>0` such that

\[
                         \mathbb E e^{-G^-(T)}
 \le e^{-c_0m}.                                      \tag{4.5}
\]

Markov's exponential bound gives

\[
 \Pr(G^-(T)<q)
 \le e^q\mathbb E e^{-G^-(T)}
 \le e^{-cm}                                         \tag{4.6}
\]

for some absolute `c>0`, uniformly over `q<=H`, because `H=o(m)`.
Multiplying by `N_q<=W` and applying Lemma 2.1 yields

\[
                         B_q^-\le e^{-cm}W.           \tag{4.7}
\]

Blockwise complementation and Lemma 2.2 give the same estimate for
`B_q^+`.  Summing (4.7) over `q<=H` proves (0.2).

## 5. Abundance of potential paths

If `G^-(T)=g`, every `q`-subset of the `g` good blocks gives a potential
lower path, and each selected local edge has two possible initial
orientations.  Hence `T` has at least

\[
                         2^q\binom gq                \tag{5.1}
\]

potential oriented realizations inside the mosaic.  The analogous upper
count is identical.  With exponentially high target density one has
`g=Theta(m)`, so (5.1) is enormous throughout every `q=o(m)` window.

This abundance alone is not sufficient.  A fixed isometric factor in a
`Q_s` cell realizes only `2^s` of the `binom(s,q)2^(s-q)` possible
depth-`q` face codes.  The exact capacity calculation below shows that no
coordination of factors inside these fixed cells can cover a typical
Gaussian profile.

## 6. Exact block-profile Hall ratio

Fix a lower target type.  Let

* `g` be its number of good singleton blocks;
* `h` its number of bad singleton blocks;
* `u` its number of local two-set blocks; and
* keep the counts of local sizes `0,3,4` fixed as part of the type.

Let `A_(g,h,u,...)` be the targets of this type.  A compatible source
owner is obtained by choosing `q` of the `g` good singleton blocks and
replacing each by one of the two endpoints of its local edge.  Its type is
therefore forced:

\[
                         (g-q,h,u+q,\ldots).          \tag{6.1}
\]

Call the corresponding owner family `S_(g,h,u,...)`.

### Lemma 6.1 (biregular compatibility graph)

The bipartite graph between `A_(g,h,u,...)` and
`S_(g,h,u,...)`, joining a target to every source from which a
return-free `q`-path can realize it, is biregular with degrees

\[
 d_A=2^q\binom gq,
 \qquad
 d_S=\binom{u+q}q.                                    \tag{6.2}
\]

Consequently

\[
 \frac{|S_{(g,h,u,\ldots)}|}{|A_{(g,h,u,\ldots)}|}
 =R_q(g,u)
 =\frac{2^q\binom gq}{\binom{u+q}q}.                 \tag{6.3}
\]

#### Proof

The target-side degree is exactly the construction in Lemma 2.1: choose
the `q` good singleton blocks and one of two source orientations in each.

A source in (6.1) has `u+q` active local two-set blocks.  Choosing any
`q` of them and toggling each once produces one target of the displayed
type; the intersection singleton of every local edge is good.  This gives
the source-side degree.  Double counting edges gives (6.3).  \(\square\)

Every source owner supplies only one directed depth-`q` window in a cycle
factor.  Sources of a different block type cannot produce a target in
`A_(g,h,u,...)`.  Therefore every product-cell factor has at least

\[
 \left(1-R_q(g,u)\right)_+|A_{(g,h,u,\ldots)}|       \tag{6.4}
\]

holes in this target type.

## 7. The Gaussian profile has ratio `e^(-6A^2)`

Let

\[
                         q=\lfloor A\sqrt m\rfloor,
 \qquad
                         p={m-q\over2m}.
\tag{7.1}
\]

Under the Bernoulli-`p` block law whose conditioning on total rank
`m-q` is uniform on the target layer, the central type values are

\[
 g_0={m\over2}\,3p(1-p)^3,
 \qquad
 u_0={m\over2}\,6p^2(1-p)^2.                         \tag{7.2}
\]

They satisfy

\[
 \frac{u_0}{2g_0}={p\over1-p}
 =1-{2A\over\sqrt m}+O(m^{-1}).                      \tag{7.3}
\]

### Lemma 7.1 (central ratio)

If `g=g_0+o(sqrt(m))` and `u=u_0+o(sqrt(m))`, then

\[
                         \log R_q(g,u)=-6A^2+o(1).    \tag{7.4}
\]

#### Proof

Write the ratio as

\[
 R_q(g,u)=\prod_{j=0}^{q-1}{2(g-j)\over u+q-j}.      \tag{7.5}
\]

Now `2g_0=3m/16+O(sqrt(m))`, while (7.3) gives

\[
                         u_0-2g_0=-{3A\over8}\sqrt m+O(1).
\tag{7.6}
\]

Thus the denominator in the `j`-th factor of (7.5) is

\[
 2g_0+{5q\over8}-j+O(1),                            \tag{7.7}
\]

whereas the numerator is `2g_0-2j+o(sqrt(m))`.  Taylor-expand the
logarithm; every individual perturbation is `O(m^(-1/2))`, and the sum of
the quadratic remainders is `o(1)`.  The linear sum is

\[
 -{1\over2g_0}\sum_{j=0}^{q-1}\left(j+{5q\over8}\right)
 =-{9q^2\over16g_0}+o(1)
 =-6A^2+o(1).                                        \tag{7.8}
\]

This proves (7.4).  \(\square\)

The fixed-dimensional conditional multinomial local limit theorem (or
Stirling's formula summed over a box of side `eta sqrt(m)`) gives the
following elementary consequence: for every fixed `A>0`, one may choose
`eta_A>0` so that a positive fraction `c_A` of all rank-`m-q` targets
have every block-type count within `eta_A sqrt(m)` of its central value,
and throughout this box

\[
                         R_q(g,u)\le e^{-3A^2}<1.     \tag{7.9}
\]

The map from a target type to its compatible source type in (6.1) is
injective.  Hence the deficits (6.4) for the types in this box can be
summed without reusing source capacity.  Since

\[
                         {N_q\over W}\longrightarrow e^{-A^2},
\tag{7.10}
\]

we obtain:

### Theorem 7.2 (linear fixed-block capacity deficit)

For every fixed `A>0` and `q=floor(A sqrt(m))`, every choice of one
spanning cycle factor in every product cell of the fixed `Q_4` mosaic
misses at least

\[
 \boxed{
 \left(c_A(1-e^{-3A^2})e^{-A^2}-o(1)\right)W}        \tag{7.11}
\]

lower targets.  The same lower bound holds for upper targets by
complementation.

Thus the local mixed-frame mosaic removes the support obstruction but not
the capacity obstruction.  Any positive recursion must change the
four-block decomposition on a non-negligible owner mass, or introduce
cycles whose windows genuinely cross the product blocks.
