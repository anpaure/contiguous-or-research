# The directed punctured-configuration hypergraph: exact pair profile and the cluster gate

**Status (2026-08-21).**  Sections 1--7 are proved/audited.  They give the exact
degrees, every pair codegree, the complete pair inventory inside one edge,
and the exact normalized internal pair-codegree mass of the direct
two-rank punctured-wreath hypergraph.  In particular,

\[
 {S(e)\over D_M}
 =12+{32\over r}+{99\over2r^2}+O(r^{-3}).                 \tag{0.1}
\]

The constant-order mass is not diffuse.  Up to `O(D_M/r)` it is carried by
two canonical paths: the alternating containment path and the middle-layer
Kneser path.  This is the first genuinely cyclic-interval feature that a
cluster-aware matching argument can use.

Section 7 audits the matching consequence.  The hypergraph has an exact
optimal fractional matching, but no published or generic growing-rank
matching theorem rounds it.  In particular, `S(e)=O(D_M)` alone is
insufficient: the common-partial-transversal construction gives regular
growing-rank hypergraphs with this local scale and a vanishing matching
ratio.  Section 8 records a sharp conditional process-specific remaining gate.  No
integral near-factor is claimed here.

## 1. Definition

Put

\[
 b=2r+1,\qquad X=[b],\qquad
 M={X\choose r},\qquad L={X\choose r-1}.                \tag{1.1}
\]

For a word `w=(w_0,...,w_{b-1})` which is a permutation of `X`, indices
being read modulo `b`, write

\[
 I_k^w(s)=\{w_s,w_{s+1},\ldots,w_{s+k-1}\}.              \tag{1.2}
\]

The directed punctured configuration indexed by `w` is

\[
 E(w)=\{(M,I_r^w(s)):s\ne0\}
       \mathbin{\dot\cup}
       \{(L,I_{r-1}^w(s)):s\ne0\}.                       \tag{1.3}
\]

Thus `E(w)` has `2r` vertices in each layer and rank `4r`.  Configurations
are initially kept with their directed word index.

The retained vertices have a useful physical order:

\[
 L_1,M_1,L_2,M_2,\ldots,L_{2r},M_{2r},                  \tag{1.4}
\]

where `L_i=I_{r-1}^w(i)` and `M_i=I_r^w(i)`.  Consecutive
vertices in (1.4) are incident in the middle inclusion graph.  Hence (1.4)
is an alternating path.  The transition is not an arbitrary Johnson step:
the inserted coordinate is removed after the prescribed FIFO delay.  This
FIFO path description is the extra structure absent from an arbitrary
regular growing-rank hypergraph.

### Proposition 1.1 (analytic injectivity of the directed deck)

The map `w -> E(w)` is injective.  Thus the configuration hypergraph is
simple and has exactly `b!` edges.

#### Proof

Given only `E(w)`, form its bipartite containment graph between the clean
lower and middle targets.  In the unpunctured cyclic deck, every
`(r-1)`-window is contained in exactly the two `r`-windows obtained by
extending it at its two ends; no other containment is possible.  This is
the alternating cycle on the full two-rank deck.  Deleting the adjacent
dirty vertices `L_0,M_0` leaves precisely the path (1.4).

The two endpoints of this path lie in different target layers, so the
orientation beginning at `L_1` is canonical.  It recovers every same-start
pair `(L_i,M_i)`.  Their singleton differences are

\[
 M_i\setminus L_i=\{w_{i+r-1}\},\qquad 1\le i\le2r.       \tag{1.5}
\]

As `i` traverses this range, the indices `i+r-1` modulo `b` are all
positions except `r-1`.  Hence (1.5) recovers the label in every word
position except `w_{r-1}`, and that last entry is the unique unused label.
The full directed word is therefore determined by `E(w)`.  \(\square\)

## 2. Degrees

### Proposition 2.1 (exact two degrees)

Every middle target and lower target have respective degrees

\[
 \begin{aligned}
 D_M&=(b-1)r!(b-r)!=2r\,r!(r+1)!,\\
 D_L&=(b-1)(r-1)!(b-r+1)!
     =2(r+2)r!(r+1)!={r+2\over r}D_M.                  \tag{2.1}
 \end{aligned}
\]

#### Proof

Fix a `k`-set `A`, with `k` equal to `r` or `r-1`.  Prescribing the
retained start of `A` gives `k!(b-k)!` words, and there are `b-1` retained
starts.  A proper nonempty subset has a unique cyclic start in any fixed
word, so there is no overcount.  Substitution gives (2.1).  \(\square\)

In particular the degree ratio is `1+2/r`; the two-layer hypergraph is
asymptotically regular.

## 3. All pair codegrees

For `1<=k,h<b`, `k+h<=b`, and `0<=a<=min(k,h)`, put

\[
 \Phi_{k,h}(a)
 :=a!(k-a)!(h-a)!(b-k-h+a)!                              \tag{3.1}
\]

and

\[
 m_{k,h}(a)=
 \begin{cases}
 b-k-h+1,&a=0,\\
 2,&1\le a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h).
 \end{cases}                                             \tag{3.2}
\]

### Theorem 3.1 (punctured cyclic-arc pair formula)

Let `A` be a `k`-set and `B` an `h`-set, with \(a=|A\cap B|\).  The number
of directed words for which both sets occur at retained starts is

\[
 d_{k,h}(a)=
 \left((b-2)m_{k,h}(a)+\mathbf1_{a=\min(k,h)}\right)
 \Phi_{k,h}(a).                                         \tag{3.3}
\]

Layer tags are understood when `k` and `h` differ.  Formula (3.3) also
returns the degree when `k=h` and `A=B`.

#### Proof

Fix positional cyclic arcs of lengths `k,h` and intersection `a`.  Once
their two starts are fixed, the four Venn cells can be labelled in exactly
`Phi_{k,h}(a)` ways.

With the first start fixed on the full cycle, the number of relative starts
giving intersection `a` is (3.2): there are `b-k-h+1` disjoint placements,
two placements for every proper positive overlap, and `|k-h|+1`
placements in which the shorter arc is contained in the longer.  Hence the
full-cycle number of ordered start pairs is `b m_{k,h}(a)`.

Delete the pairs whose first or second start is zero.  Each deleted fibre
has size `m_{k,h}(a)`.  The pair `(0,0)` was deleted twice and must be put
back precisely when the overlap is `min(k,h)`.  The retained positional
factor is therefore `(b-2)m+1_{a=min(k,h)}`, proving (3.3).  \(\square\)

Specializing (3.3) gives the following complete table for distinct
vertices:

\[
\begin{array}{c|c|c|c}
\text{layers}&a&\text{positional factor }n(a)&
 d(a)/n(a)\\ \hline
MM&0\le a\le r-1&4r-2&a!(r-a)!^2(a+1)!\\
LL&a=0&8r-4&(r-1)!^2\,3!\\
LL&1\le a\le r-2&4r-2&a!(r-1-a)!^2(a+3)!\\
ML&a=0&6r-3&r!(r-1)!\,2!\\
ML&1\le a\le r-2&4r-2&a!(r-a)!(r-1-a)!(a+2)!\\
ML&a=r-1&4r-1&(r-1)!(r+1)!.
\end{array}                                               \tag{3.4}
\]

For `r>=3`, the maximum pair codegree is the last entry, namely

\[
 \Delta_2=(4r-1)(r-1)!(r+1)!,\qquad
 {\Delta_2\over D_L}={4r-1\over2r(r+2)}\sim {2\over r}.
                                                               \tag{3.5}
\]

To verify maximality, in each row of (3.4) the ratio of successive
factorial terms is monotone, so a maximum is at an endpoint.  Comparing
the finitely many endpoints gives (3.5).  For `r=2`, the disjoint `LL`
pair is the exceptional maximum.

## 4. Pair inventory inside one configuration

Coordinate relabelling is transitive on directed words, so it suffices to
use the identity word.  Let `c_{XY}(a)` be the number of unordered pairs
of layer types `X,Y` and intersection `a` inside a fixed edge.

### Proposition 4.1 (exact inventory)

\[
\begin{array}{c|c|c}
\text{layers}&a&c_{XY}(a)\\ \hline
MM&0\le a\le r-1&2r-1\\
LL&a=0&4r-2\\
LL&1\le a\le r-2&2r-1\\
ML&a=0&6r-3\\
ML&1\le a\le r-2&4r-2\\
ML&a=r-1&4r-1.
\end{array}                                               \tag{4.1}
\]

#### Proof

The ordered retained-start count in Theorem 3.1, before multiplication by
the Venn-cell labelling factor, is exactly the number of ordered pairs of
the corresponding positional arcs in the identity edge.  Divide by two
for equal-layer unordered pairs and do not divide for a cross-layer pair.
This gives (4.1).  The row sums are respectively
`binom(2r,2)`, `binom(2r,2)`, and `(2r)^2`, as required.  \(\square\)

## 5. Exact internal pair-codegree mass

Define

\[
 S(e)=\sum_{\{u,v\}\in{e\choose2}}d(u,v)
      =S_{MM}+S_{ML}+S_{LL}.                              \tag{5.1}
\]

For compactness put

\[
\begin{aligned}
n_{ML}(a)&=
 \begin{cases}3(2r-1),&a=0,\\2(2r-1),&1\le a\le r-2,\\
 4r-1,&a=r-1,\end{cases}\\
n_{LL}(a)&=
 \begin{cases}4(2r-1),&a=0,\\2(2r-1),&1\le a\le r-2.
 \end{cases}                                             \tag{5.2}
\end{aligned}
\]

### Theorem 5.1 (exact normalized mass)

For every directed punctured configuration,

\[
 {S_{MM}\over D_M}
 ={(2r-1)^2\over r}
 \sum_{a=0}^{r-1}{1\over {r\choose a}{r+1\choose a+1}}, \tag{5.3}
\]

\[
 {S_{ML}\over D_M}
 ={1\over2r}\sum_{a=0}^{r-1}
 {n_{ML}(a)^2\over {r\choose a}{r+1\choose a+2}},       \tag{5.4}
\]

and

\[
 {S_{LL}\over D_M}
 ={r+2\over4r^2}\sum_{a=0}^{r-2}
 {n_{LL}(a)^2\over {r-1\choose a}{r+2\choose a+3}}.     \tag{5.5}
\]

Consequently

\[
\begin{aligned}
{S_{MM}\over D_M}&=4-{4\over r}+{9\over r^2}+O(r^{-3}),\\
{S_{ML}\over D_M}&=8+{32\over r}-{111\over2r^2}+O(r^{-3}),\\
{S_{LL}\over D_M}&={4\over r}+{96\over r^2}+O(r^{-3}),
                                                               \tag{5.6}
\end{aligned}
\]

and hence (0.1).

#### Proof

Multiply each entry of (3.4) by its inventory in (4.1), divide by
`D_M`, and use

\[
 {a!(r-a)!^2(a+1)!\over r!(r+1)!}
 ={1\over {r\choose a}{r+1\choose a+1}},                \tag{5.7}
\]

\[
 {a!(r-a)!(r-1-a)!(a+2)!\over r!(r+1)!}
 ={1\over {r\choose a}{r+1\choose a+2}},                \tag{5.8}
\]

and

\[
 {a!(r-1-a)!^2(a+3)!\over r!(r+1)!}
 ={r+2\over r}
 {1\over {r-1\choose a}{r+2\choose a+3}}.              \tag{5.9}
\]

This proves (5.3)--(5.5).

For the expansion, isolate the endpoint terms in the three reciprocal
binomial sums.  The required elementary estimates are

\[
 \sum_{a=0}^{r-1}{1\over {r\choose a}{r+1\choose a+1}}
 ={1\over r}+{2\over r^3}+O(r^{-4}),                    \tag{5.10}
\]

while in (5.4) the containment term, the disjoint term, and the
`a=r-2` term contribute respectively

\[
 8-{4\over r}+{1\over2r^2},\qquad
 {36\over r}-{72\over r^2}+O(r^{-3}),\qquad
 {16\over r^2}+O(r^{-3}).                               \tag{5.11}
\]

All other terms in (5.4) total `O(r^-3)`.  In (5.5), the `a=r-2`
and `a=0` terms are

\[
 {4\over r}+O(r^{-3}),\qquad {96\over r^2}+O(r^{-3}),   \tag{5.12}
\]

and the remaining terms total `O(r^-3)`.  The error estimates follow
either from successive-term ratios or from the elementary lower bounds on
the relevant binomial coefficients.  Substitution yields (5.6).  \(\square\)

The exact values for `r=2,3,4,5` are

\[
 {S(e)\over D_M}
 =24.125,\quad24.546296\ldots,\quad22.65,\quad20.549.    \tag{5.13}
\]

These are exhaustive word counts, not Monte Carlo estimates.

## 6. The cyclic high-overlap skeleton

Inside `E(w)`, let `Gamma_w` contain

1. every containment pair `L subset M`; and
2. every disjoint pair of middle targets.

### Theorem 6.1 (two-path concentration of pair mass)

The containment edges of `Gamma_w` form the alternating path (1.4), with
`4r-1` edges.  The disjoint middle pairs form a path on the `2r` retained
middle windows, with `2r-1` edges.  Thus

\[
 |E(\Gamma_w)|=6r-2,\qquad \Delta(\Gamma_w)\le4.          \tag{6.1}
\]

Moreover

\[
 {1\over D_M}\sum_{uv\in E(\Gamma_w)}d(u,v)
 ={(2r-1)^2\over r(r+1)}+{(4r-1)^2\over2r^2}
 =12-{12\over r}+{19\over2r^2}+O(r^{-3}),               \tag{6.2}
\]

whereas

\[
 {1\over D_M}\sum_{uv\in {E(w)\choose2}\setminus E(\Gamma_w)}d(u,v)
 ={44\over r}+{40\over r^2}+O(r^{-3}).                  \tag{6.3}
\]

Every off-skeleton pair has codegree `O(D_M/r^2)`; asymptotically the
largest off-skeleton type is the disjoint `ML` type, with relative codegree

\[
 {3(2r-1)\over r^2(r+1)}=(6+o(1))r^{-2}.                \tag{6.4}
\]

#### Proof

The containment assertion follows directly from (1.4).  In the full
middle cyclic deck, disjointness joins successive vertices in the usual
odd-graph cyclic order.  Deleting the punctured middle window breaks this
cycle into a path.

The two mass contributions are the `MM,a=0` and `ML,a=r-1` entries of
(3.4)--(4.1), giving the two exact summands in (6.2).  Subtract (6.2)
from Theorem 5.1 to obtain (6.3).  Finally, endpoint comparison in each
row of (3.4), after excluding the two skeleton types, gives (6.4) and the
stated `O(D_M/r^2)` bound.  \(\square\)

Thus the constant `12` in (0.1) is the mass of a bounded-degree,
one-dimensional cluster skeleton, not a dense common core.  A proof which
uses only the scalar `S(e)` discards precisely this information.

There is also a useful conflict-count consequence.  Let `C(e)` be the
number of other indexed configurations meeting `e`, and put

\[
 A(e)=\sum_{v\in e}(d(v)-1)=2r(D_M+D_L)-4r.              \tag{6.5}
\]

Since `x-1<=binom(x,2)` for `x>=1`,

\[
 A(e)-\left(S(e)-{4r\choose2}\right)\le C(e)\le A(e).  \tag{6.6}
\]

In particular

\[
 C(e)=4(r+1)D_M\left(1+O(r^{-1})\right).                \tag{6.7}
\]

So, conditional on meeting `e`, all but an `O(1/r)` proportion of
intersection incidences come from configurations meeting `e` only once.

### Corollary 6.2 (exactly calibrated initial slow bite)

Fix a constant `gamma>0`.  Mark every configuration independently with

\[
 p={\gamma\over rD_M},                                   \tag{6.8}
\]

and retain a marked configuration iff no other marked configuration meets
it.  The retained configurations form a matching.  A fixed configuration
is retained with probability

\[
 p(1-p)^{C(e)}
 ={\gamma\over rD_M}\exp(-4\gamma+o(1)).                 \tag{6.9}
\]

Consequently the expected covered fractions in `M` and `L` are
respectively

\[
 {\gamma e^{-4\gamma}+o(1)\over r},\qquad
 {r+2\over r}{\gamma e^{-4\gamma}+o(1)\over r}.          \tag{6.10}
\]

#### Proof

Conditional on marking `e`, the marks on its `C(e)` distinct neighbours
are independent.  Equations (6.7)--(6.8), together with
`p^2C(e)=o(1)`, give (6.9).  Isolated marked configurations are pairwise
disjoint.  Finally, the numbers of configuration incidences per target are
`D_M,D_L`, so multiplying (6.9) by those degrees yields (6.10).
\(\square\)

## 7. Fractional optimum and matching-theorem audit

### Proposition 7.1 (exact optimal fractional matching)

Give every indexed configuration weight `1/D_L`.  Every lower vertex then
has load one and every middle vertex has load

\[
 {D_M\over D_L}={r\over r+2}.                            \tag{7.1}
\]

The total weight is

\[
 {b!\over D_L}={|L|\over2r}.                             \tag{7.2}
\]

This is optimal, because every integral or fractional edge uses `2r`
lower vertices and the total lower capacity is `|L|`.  Thus the exact
integral target is to round the constant fractional solution while losing
only `o(|L|)` lower vertices.  The unavoidable excess middle vertices are
only a `2/(r+2)=o(1)` fraction of `M`.

### Why existing black boxes do not round (7.2)

Let `k=4r` and `Delta=D_L`.  From (3.5),

\[
 k{\Delta_2\over\Delta}
 ={2(4r-1)\over r+2}\longrightarrow8.                  \tag{7.3}
\]

Pippenger--Spencer and its standard refinements first fix `k`; their
degree thresholds are not uniform in the diagonal `k=4r`.  The
small-codegree quantitative bounds of Vu/Kostochka--Rodl formally contain

\[
 (\Delta/\Delta_2)^{-1/(k-1)}
 =\exp\!\left(-(1+o(1)){\log r\over4r}\right)=1-o(1),   \tag{7.4}
\]

so even suppressing all hidden `k`-dependence gives no vanishing leave.
The explicit growing-uniformity hypotheses with an `exp(O(k))` loss also
fail because `Delta_2/Delta=Theta(1/r)`, not exponentially small in `k`.

Nor does (0.1) by itself imply a matching theorem.  The proved
common-partial-transversal construction produces exactly regular
growing-rank hypergraphs with arbitrarily large degree, `S(e)=O(D)`, and
even a vanishing squared local codegree kernel, but every matching covers
only `o(1)` of the vertices.  Its obstruction is a latent system of common
equipartitions, invisible to all one-edge pair statistics.

Therefore the following implications are invalid:

\[
 \Delta_2/\Delta=o(1)\ \Longrightarrow\ \nu\sim\nu^*,
 \qquad
 S(e)=O(\Delta)\ \Longrightarrow\ \nu\sim\nu^*.        \tag{7.5}
\]

The exact profile nevertheless improves the live target: a specialized
proof may expose the two paths in `Gamma_w` as local clusters and treat the
remaining interactions at the `D_M/r^2` scale.  It must additionally use a
global anti-partition property of cyclic interval decks.

## 8. A sharp process-specific regeneration gate

This section isolates one sufficient statement whose proof would turn the
preceding exact arithmetic into the required `o(1)` matching leave.

After a matching has removed the same number of vertices from `M` and `L`,
write the lower residual density as `x`.  The middle residual density is
forced to be

\[
 y={rx+2\over r+2},                                    \tag{8.1}
\]

because `|M|/|L|=(r+2)/r`.  Independent thinning at these two densities
predicts residual degrees

\[
\begin{aligned}
d_x(v)&=D_Lx^{2r-1}y^{2r} &&(v\in L),\\
d_x(v)&=D_Mx^{2r}y^{2r-1} &&(v\in M).                  \tag{8.2}
\end{aligned}
\]

Use the middle expression as the common residual degree scale,

\[
 d_x:=D_Mx^{2r}y^{2r-1}.                                \tag{8.3}
\]

For `x>=r^{-alpha}` with fixed `alpha<1`, the two quantities in (8.2)
have ratio `1+o(1)`, so this convention is immaterial.  If `e` is a
surviving configuration and `F` ranges over surviving configurations, put

\[
 t_F(e):=|e\cap F|,qquad
 \mathfrak E_x(e):=\sum_{F:t_F(e)>0}\bigl(t_F(e)-1\bigr). \tag{8.4}
\]

The quantity `mathfrak E_x(e)` is the exact duplicate excess when the
incident configuration stars of the targets in `e` are united.  Indeed,
the total conflict incidence is `sum_F t_F(e)=Theta(r d_x)`, while the
number of distinct incident configurations is `sum_F 1_{t_F(e)>0}`; their
difference is (8.4).

Fix any constant `alpha<1/2`, for example `alpha=1/3`.

> **Quenched FIFO regeneration gate `QFR(alpha)`.**  A slow isolated-edge
> bite, run for `O(r log r)` rounds, can be coupled so that, uniformly until
> `x=r^{-alpha}`, every surviving target has degree `(1+o(1))` times (8.2),
> and every surviving edge satisfies the precise duplicate-excess estimate
> \[
>       \mathfrak E_x(e)=o(r d_x).                         \tag{8.5}
> \]
> Equivalently, configurations causing two or more simultaneous target
> conflicts contribute an `o(1)` fraction of total conflict incidence.
> The errors are uniform over all rounds and both layers.

### Proposition 8.1 (the gate implies a vanishing leave)

`QFR(alpha)` implies a matching of size

\[
 (1-r^{-\alpha}+o(1)){|L|\over2r};                     \tag{8.6}
\]

hence an `o(1)` lower leave and, by (8.1), an `o(1)` middle leave.

#### Proof

In a residual satisfying the gate, fix a constant `gamma>0` and mark each
configuration independently with

\[
 p_x={\gamma\over r d_x}.                               \tag{8.7}
\]

The last clause and the same Bonferroni calculation as (6.6) show that a
marked edge is isolated with probability bounded below by an absolute
constant.  Equations (8.2) make the bite remove a
`Theta(1/r)` fraction of the remaining lower vertices, with the same
absolute number removed from the middle layer.  Therefore `O(r log r)`
bites reduce `x` from one to `r^{-alpha}`.

There is ample degree throughout this trajectory.  Stirling's formula and
`y=(1+o(1))x` for `x>=r^{-alpha}` give

\[
 \log\!\left(D_Mx^{2r}y^{2r}\right)
 =(2-4\alpha+o(1))r\log r,                              \tag{8.8}
\]

which tends to infinity for `alpha<1/2`.  Thus the stipulated uniform
errors do not run out of degree before the stopping density.  The residual
sizes at the stop give (8.6).  \(\square\)

The point of `QFR(alpha)` is that it is narrower than a new general
growing-rank Pippenger theorem.  Here every edge is simultaneously

1. a FIFO alternating path in the inclusion graph;
2. a path in the middle odd graph on its high-codegree disjoint pairs; and
3. an `S_b`-exchangeable relabelling of this two-path object.

Those are the features available for a transfer-matrix, cluster-expansion,
or trajectory martingale proof.  The common-partial-transversal
counterexample has none of this relabelled FIFO geometry and specifically
fails the quenched regeneration conclusion.  Proving `QFR(alpha)`, or an
equivalent direct anti-partition theorem for these cyclic interval decks,
is the exact remaining matching task on this route.

## 9. Reproducibility

The independent exhaustive checker is

`scratch/audit_direct_punctured_configuration_pair_profile_20260821.py`.

The larger intersection census used as a cross-check is

`scratch/research_punctured_configuration_intersection_profile_20260821.cpp`.

On H100, the exhaustive `r=4` and `r=5` runs inspect respectively
`9!=362880` and `11!=39916800` directed configurations and return

```text
r=4  pair_sum=521856    S_over_Dmiddle=22.65
r=5  pair_sum=17754336  S_over_Dmiddle=20.549
```

Every category count and pair codegree agrees with (3.4) and (4.1).
