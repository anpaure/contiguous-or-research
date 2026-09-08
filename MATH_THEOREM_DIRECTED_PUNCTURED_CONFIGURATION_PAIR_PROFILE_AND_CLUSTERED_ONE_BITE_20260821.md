# Exact pair profile of the directed punctured-configuration hypergraph

**Date:** 2026-08-21  
**Status:** unconditional codegree, internal-moment, cluster-localization, and
one-bite theorem; an iterative near-perfect matching theorem remains open

## 1. The configuration hypergraph

Put

\[
 b=2r+1,\qquad r\ge2.
\]

A directed configuration is a linear permutation `w` of `[b]`.  At each
cyclic start `i=1,...,2r`, retain its rank-`r` window `M_i` and its
rank-`(r-1)` window `L_i`; start zero is dirty in both layers.  Let
`C_r` be the indexed `4r`-uniform multi-hypergraph on

\[
 \mathcal M=\binom{[b]}r,
 \qquad
 \mathcal L=\binom{[b]}{r-1},                               \tag{1.1}
\]

whose `b!` indexed edges are

\[
 E(w)=\{M_i,L_i:1\le i\le2r\}.                              \tag{1.2}
\]

Its two vertex degrees are

\[
 D_M=2r\,r!(r+1)!,
 \qquad
 D_L=2(r+2)r!(r+1)!={r+2\over r}D_M.                        \tag{1.3}
\]

All codegrees below count indexed configurations, including parallel
copies if they existed.  In fact the next proposition shows that they do
not.

### Proposition 1.1 (the directed target deck is injective)

The map `w -> E(w)` is injective.  Hence \(\mathcal C_r\) is simple and has
exactly `b!` edges.

#### Proof

Given only `E(w)`, form its bipartite containment graph between the clean
lower and middle targets.  A cyclic `(r-1)`-window lies in exactly the two
cyclic `r`-windows obtained by extending it at its two ends.  Before
puncturing this is the alternating cycle

\[
 M_0,L_1,M_1,L_2,\ldots,M_{b-1},L_0,M_0.
\]

Deleting the adjacent dirty vertices `M_0,L_0` leaves the path

\[
 L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r}.                     \tag{1.4}
\]

Its endpoints lie in different target layers, so (1.4) has a canonical
orientation and recovers every same-start pair `(L_i,M_i)`.  The successive
singleton differences

\[
                    M_i-L_i=\{w_{i+r-1}\},\qquad1\le i\le2r,
                                                                    \tag{1.5}
\]

recover all coordinates of the linear word except `w_{r-1}`; that last
coordinate is the unique unused label.  Thus `w` is recovered uniquely.
`square`

## 2. Complete pair-codegree table

Write `s=|X intersection Y|` and put `c=2r-1=b-2`.

### Theorem 2.1 (exact pair codegrees)

For two distinct middle targets,

\[
 \lambda_{MM}(s)
 =2c\,((r-s)!)^2s!(s+1)!,
 \qquad 0\le s\le r-1.                                     \tag{2.1}
\]

For two distinct lower targets,

\[
 \lambda_{LL}(s)=
 \begin{cases}
 24c\,((r-1)!)^2,&s=0,\\
 2c\,((r-1-s)!)^2s!(s+3)!,&1\le s\le r-2.
 \end{cases}                                                \tag{2.2}
\]

For a middle target `M` and a lower target `L`,

\[
 \lambda_{ML}(s)=
 \begin{cases}
 6c\,r!(r-1)!,&s=0,\\
 2c\,(r-s)!(r-1-s)!s!(s+2)!,&1\le s\le r-2,\\
 (4r-1)(r-1)!(r+1)!,&s=r-1.
 \end{cases}                                                \tag{2.3}
\]

In the last line, `s=r-1` is exactly the containment case `L subset M`.
Pairs outside these ranges have codegree zero.  For `r>=3`, the maximum
pair codegree is the containment value

\[
 \Delta_2=(4r-1)(r-1)!(r+1)!,
 \qquad
 {4r\Delta_2\over D_M}=8-{2\over r}.                        \tag{2.4}
\]

For `r=2`, the sole exception is
`Delta_2=lambda_LL(0)=72`; all asymptotic statements below concern
`r->infinity`.

#### Proof

First ignore the dirty start and count oriented cyclic orders modulo
rotation.  If two nonnested cyclic intervals have Venn-region sizes

\[
 a=|X-Y|,\quad s=|X\cap Y|,\quad d=|Y-X|,\quad
 u=|[b]-(X\cup Y)|,
\]

with `s>0`, their four regions must occur in one of the two cyclic orders

\[
 A,S,D,U\qquad\hbox{or}\qquad A,U,D,S.
\]

Thus their cyclic-order count is `2a!s!d!u!`.  If `s=0`, contract the two
disjoint intervals: the count is

\[
                         |X|!|Y|!(u+1)!.                    \tag{2.5}
\]

Their two window starts are distinct, so exactly `b-2=c` rotations keep
both starts clean.  Substitution gives (2.1), both noncontainment lines of
(2.2), and the first two lines of (2.3).  At `LL,s=0`, (2.5) has `u=3`
and supplies the exceptional factor `4!=24`.

It remains to count `L subset M`.  The unique point of `M-L` must occur at
one of the two ends of the middle interval.  Each end choice gives
`(r-1)!(r+1)!` cyclic orders.  In one choice the two starts coincide, so
`b-1=2r` rotations are clean; in the other they are distinct, so `b-2`
rotations are clean.  Their sum is the last line of (2.3).

For the maximum, the factorial ratios in (2.1)--(2.3) are log-convex in
`s`, so each row is maximized at an endpoint.  Direct comparison of those
finitely many endpoints gives the containment value.  Dividing it by
(1.3) proves (2.4). `square`

## 3. Pair categories inside one configuration

Fix one edge `E=E(w)`.  Cyclic distance between clean starts gives the
following exact category counts:

\[
\begin{array}{c|c|c}
\text{layers}&\text{intersection}&\text{number inside }E\\ \hline
MM&s=0,1,\ldots,r-1&c\text{ for every }s\\
LL&s=0&2c\\
LL&s=1,\ldots,r-2&c\text{ for every }s\\
ML&s=0&3c\\
ML&s=1,\ldots,r-2&2c\text{ for every }s\\
ML&s=r-1&4r-1.
\end{array}                                                  \tag{3.1}
\]

Indeed, two equal-length clean intervals have each cyclic distance
`1,...,r` exactly `c` times after start zero is removed.  For `LL`, the
last two distances are disjoint.  For `ML`, two relative starts give
containment, three give disjointness, and each remaining intersection size
has two relative starts; the coincident-start containment class has `b-1`
rather than `b-2` placements.  These observations give (3.1), whose entries
sum to `binom(2r,2)`, `binom(2r,2)`, and `4r^2` in the three layer pairs.

### Theorem 3.1 (exact internal pair-codegree sum)

For every indexed configuration edge,

\[
 S_r:=\sum_{\{X,Y\}\in\binom E2}\deg_{\mathcal C_r}(X,Y)
       =S_{MM}+S_{LL}+S_{ML},                               \tag{3.2}
\]

where

\[
\begin{aligned}
 S_{MM}
 &=2c^2\sum_{s=0}^{r-1}((r-s)!)^2s!(s+1)!,\\
 S_{LL}
 &=48c^2((r-1)!)^2
   +2c^2\sum_{s=1}^{r-2}((r-1-s)!)^2s!(s+3)!,\\
 S_{ML}
 &=18c^2r!(r-1)!+(4r-1)^2(r-1)!(r+1)!\\
 &\hspace{18mm}
   +4c^2\sum_{s=1}^{r-2}(r-s)!(r-1-s)!s!(s+2)!.
                                                               \tag{3.3}
\end{aligned}
\]

Empty sums are zero.  Moreover,

\[
 \boxed{\qquad
 {S_r\over D_M}=12+{32\over r}+O(r^{-2}).
 \qquad}                                                     \tag{3.4}
\]

In particular `S_r=O(D_M)`, although the edge rank is `4r`.

#### Proof

Multiplying the table (2.1)--(2.3) by (3.1) gives (3.3).

For the asymptotic, the normalized middle--middle sum is

\[
 {S_{MM}\over D_M}
 ={c^2\over r(r+1)}
   \sum_{s=0}^{r-1}{s+1\over\binom rs^2}
 =4-{4\over r}+O(r^{-2}).                                  \tag{3.5}
\]

Here the displayed binomial sum is `1+1/r+O(r^-2)`; after its two endpoint
terms are removed, the bound follows directly from
`binom(r,s)>=binom(r,2)` for `2<=s<=r-2`, with `s=1` handled separately.

For the mixed layer, the containment and disjoint terms respectively are

\[
 {(4r-1)^2\over2r^2},
 \qquad
 {9c^2\over r^2(r+1)},                                      \tag{3.6}
\]

while its remaining sum, after division by `D_M`, is

\[
 {2c^2\over r}\sum_{s=1}^{r-2}
 {1\over\binom rs\binom{r+1}{s+2}}
 =O(r^{-2}).                                                 \tag{3.7}
\]

Successive-term ratios, split at the middle index, bound (3.7) by a
constant times its two endpoint terms.  Hence

\[
 {S_{ML}\over D_M}=8+{32\over r}+O(r^{-2}).                 \tag{3.8}
\]

Finally, the `s=r-2` term of the lower--lower sum is

\[
 {c^2\over r^2(r-1)}={4\over r}+O(r^{-2}),                  \tag{3.9}
\]

The complete normalized non-disjoint sum is

\[
 {c^2\over r^2}\sum_{s=1}^{r-2}
 {r-1-s\over\binom{r-1}s\binom{r+1}{s+3}}.                 \tag{3.10}
\]

After the last term in (3.10) is removed, successive-term ratios from its
two ends give `O(r^-2)`; the disjoint term is also `O(r^-2)`.  Thus

\[
 {S_{LL}\over D_M}={4\over r}+O(r^{-2}).                    \tag{3.11}
\]

Adding (3.5), (3.8), and (3.11) proves (3.4). `square`

## 4. The two large-codegree clusters are paths

The asymptotic mass `12D_M` is not diffuse.

### Proposition 4.1 (exact path localization)

Inside `E(w)`:

1. the `4r-1` containment pairs `L subset M` form one path on all `4r`
   clean targets; and
2. the `2r-1` disjoint `MM` pairs form one path on the `2r` clean middle
   targets.

Their internal codegree masses are respectively

\[
 S_{\rm contain}=(4r-1)^2(r-1)!(r+1)!,
 \qquad
 S_{\rm disjMM}=2c^2(r!)^2,                                 \tag{4.1}
\]

and therefore

\[
 {S_{\rm contain}\over D_M}=8-{4\over r}+O(r^{-2}),
 \qquad
 {S_{\rm disjMM}\over D_M}=4-{8\over r}+O(r^{-2}).         \tag{4.2}
\]

All remaining pair-codegree mass is only

\[
              S_r-S_{\rm contain}-S_{\rm disjMM}
              =O(D_M/r).                                    \tag{4.3}
\]

#### Proof

Before puncturing, containment between the `M_i` and `L_i` windows is an
alternating cycle: each `L_i` lies in the two middle windows obtained by
extending it at its left or right end.  Removing the two dirty vertices at
start zero deletes two adjacent vertices of that cycle and leaves a path
on `4r` vertices.  Likewise, disjointness on the `b` middle windows is the
step-`r` cycle; deleting `M_0` leaves a path on `2r` vertices.  Equations
(4.1)--(4.3) now follow from (2.1), (2.3), and Theorem 3.1. `square`

## 5. What the profile does prove for a nibble

Let

\[
 \Gamma(E)=\{F\in E(\mathcal C_r):F\cap E\ne\varnothing\}
\]

count indexed neighboring configurations, including `E`.  Put
`t_F=|E intersection F|`.  Then

\[
 \sum_{X\in E}\deg(X)-|\Gamma(E)|
 =\sum_{F:t_F>0}(t_F-1).
\]

Since `t-1<=binom(t,2)`, Theorem 3.1 gives

\[
 0\le4(r+1)D_M-|\Gamma(E)|\le S_r=O(D_M).                   \tag{5.1}
\]

Here `sum_{X in E}deg(X)=2r(D_M+D_L)=4(r+1)D_M`.

### Corollary 5.1 (constant-survival one bite)

Fix a constant `alpha>0`, independently mark every indexed configuration
with probability

\[
                         p={\alpha\over rD_M},               \tag{5.2}
\]

and retain a marked configuration exactly when no other marked
configuration meets it.  Then a fixed configuration is retained with
probability

\[
 p(1-p)^{|\Gamma(E)|-1}
 ={\alpha\over rD_M}\exp(-4\alpha+o(1)).                    \tag{5.3}
\]

The retained configurations form a matching.  The expected fractions of
the middle and lower target layers covered in this bite are respectively

\[
 {\alpha e^{-4\alpha}+o(1)\over r},
 \qquad
 {r+2\over r}\,{\alpha e^{-4\alpha}+o(1)\over r}.          \tag{5.4}
\]

#### Proof

The neighbor marks are independent, so (5.3) is exact before its
asymptotic simplification; use (5.1) and `p^2|Gamma(E)|=o(1)`.  The retained
edges are pairwise disjoint by definition.  Finally double count the
`2r` incidences in each target layer:

\[
 {|E(\mathcal C_r)|\,2r\over|\mathcal M|}=D_M,
 \qquad
 {|E(\mathcal C_r)|\,2r\over|\mathcal L|}=D_L,
\]

and substitute (1.3). `square`

## 6. Exact remaining dynamic gate

Equations (4.3) and (5.3) show why the constant value
`4r Delta_2/D_M -> 8` is not by itself fatal: the large pair dependencies
are two one-dimensional paths, and an initial bite still accepts the
correct `Theta(1/r)` fraction of targets with constant survival
probability.

They do **not** prove that `Theta(r log r)` successive bites remain
quasirandom.  An average internal-codegree hypothesis cannot do so: the
common-partial-transversal counterexample with gadget degree `D=r^2`, rank
`r`, and absolute pair codegree at most two has `S(E)=O(D)` but matching
density `o(1)`.

For `\mathcal C_r`, the configuration-specific positive target is now a
dynamic interval-cluster lemma: until both residual layer densities reach
`r^{-1/2+epsilon}`, it should keep every surviving configuration degree and
both path-cluster exposure counts within `1+o(1)` of their trajectory.
At that stopping density the uncovered fraction is already `o(1)`, while
the nominal residual degree remains exponential because

\[
 D_M\bigl(r^{-1/2+\epsilon}\bigr)^{4r}
   =\exp\bigl((4\epsilon+o(1))r\log r\bigr).                 \tag{6.1}
\]

Proving this martingale/switching statement would turn Corollary 5.1 into a
near-perfect matching.  No currently frozen generic growing-rank theorem
implies it; the two cyclic-window paths in Proposition 4.1 must be used.
