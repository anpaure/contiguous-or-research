# Aggregate-linear packet reservoirs and deterministic anchored fans

## Status

This note gives two quantitative integral consequences of the exact packet
degree ledger.

1.  The aggregate collision mass `Xi=o(1)` produces, by one independent
    sampling and alteration, a **linear** packet reservoir which is
    `rho`-regular on all but an explicitly bounded exceptional set.
2.  The sharp pair codegree `Delta_2/D_0=2/r` gives a deterministic bank of
    pairwise resource-disjoint packets through any prescribed
    `Theta(r/L)=Theta(sqrt r)` resource anchors.

These are genuine growing-uniformity statements; no fixed-rank nibble is
invoked.  They are not a near-perfect packet factor.  Singleton packet
intersections still dominate the matching process, and the lower named
targets have intentional containment codegrees.  The last section records
these two exact limits.

## 1. A general alteration lemma

Let `H` be a simple `h`-uniform, `D`-regular hypergraph on `N` vertices.
For an edge `e`, define

\[
 \Xi(e)={1\over D}\sum_{\{x,y\}\in\binom e2}d_H(x,y),
 \qquad \Xi=\max_e\Xi(e).                                  \tag{1.1}
\]

The summand includes `e` itself.  Put

\[
 \mathcal B(e)=\{f\ne e:|e\cap f|\ge2\}.                 \tag{1.2}
\]

### Lemma 1.1 (the double-overlap halo)

For every edge `e`,

\[
                         |\mathcal B(e)|\le D\Xi.          \tag{1.3}
\]

#### Proof

Every `f` in `mathcal B(e)` contains at least one pair from `e`.  Hence

\[
 |\mathcal B(e)|
 \le \sum_{\{x,y\}\in\binom e2}(d_H(x,y)-1)
 \le D\Xi.                                                \tag{1.4}
\]

`square`

### Theorem 1.2 (aggregate-linear random reservoir)

Let

\[
 0<\varepsilon<\tfrac12,qquad
 1\le\rho\le D/2,qquad
 \rho\Xi\le\tfrac18,qquad
 {N\rho\over h}\ge64.                                    \tag{1.5}
\]

Then `H` contains a linear subhypergraph `R` with

\[
                         |R|\ge {N\rho\over4h},             \tag{1.6}
\]

such that, outside a vertex set `Z` of size at most

\[
 |Z|\le
 8N\exp(-\varepsilon^2\rho/3)
       +{2N\rho\Xi\over\varepsilon},                      \tag{1.7}
\]

every vertex has reservoir degree

\[
                 (1-2\varepsilon)\rho
        \le d_R(v)\le(1+\varepsilon)\rho.                 \tag{1.8}
\]

Here *linear* means that two distinct edges of `R` meet in at most one
vertex.

#### Proof

Select every edge independently with probability

\[
                              p={\rho\over D}.              \tag{1.9}
\]

Let `X` be the number selected.  Since `|E(H)|=ND/h`,

\[
                              \mathbb EX={N\rho\over h}=:\mu.\tag{1.10}
\]

Let `Y` count unordered selected pairs which meet in at least two
vertices.  Lemma 1.1 gives

\[
 \mathbb EY
 \le {1\over2}|E(H)|D\Xi p^2
 ={N\rho^2\Xi\over2h}.                                    \tag{1.11}
\]

For a vertex `v`, its selected degree is `Bin(D,p)`, of mean `rho`.
Let `Z_0` be the number of vertices whose selected degree is outside
`[(1-epsilon)rho,(1+epsilon)rho]`.  Chernoff's inequality gives

\[
                    \mathbb EZ_0
       \le2N\exp(-\varepsilon^2\rho/3).                    \tag{1.12}
\]

The lower-tail Chernoff bound, (1.11), (1.12), and Markov's inequality
show that with positive probability all three inequalities

\[
 X\ge\mu/2,qquad
 Y\le {2N\rho^2\Xi\over h},
 \qquad
 Z_0\le8N\exp(-\varepsilon^2\rho/3)                       \tag{1.13}
\]

hold simultaneously.  Indeed, under `mu>=64`, the first failure has
probability less than `1/4`, and each of the other two failures has
probability at most `1/4`.

Fix such an outcome.  In the graph whose vertices are the selected
packets and whose edges are the double-overlap pairs, choose one endpoint
of every graph edge and delete the union of the chosen endpoints.  At most
`Y` packets are deleted, and the remaining packet hypergraph is linear.
By (1.5) and (1.13),

\[
 |R|\ge {N\rho\over2h}-{2N\rho^2\Xi\over h}
       \ge {N\rho\over4h}.                                \tag{1.14}
\]

At most `hY<=2Nrho^2Xi` vertex-packet incidences were deleted.  Thus the
number of vertices losing more than `epsilon rho` incidences is at most

\[
                         {2N\rho\Xi\over\varepsilon}.       \tag{1.15}
\]

Outside these vertices and those counted by `Z_0`, the old degree bounds
lose at most `epsilon rho` on the lower side and nothing on the upper
side.  This proves (1.7)--(1.8).  `square`

## 2. Specialization to the parity-unified pull-ring packets

For the packet hypergraph in
`MATH_THEOREM_PARITY_UNIFIED_OWNER_Q1_RING_PACKET_DEGREES_CODEGREES_AND_FRACTIONAL_FACTOR_20260806.md`,

\[
 h=2L=\Theta(\sqrt r),\qquad D=D_0,qquad
 \Xi=O(L/r)=O(r^{-1/2}).                                  \tag{2.1}
\]

Take

\[
                 \rho=r^{1/4},\qquad\varepsilon=r^{-1/16}.\tag{2.2}
\]

### Corollary 2.1 (a polynomial-degree linear packet reservoir)

For all sufficiently large `r`, there is a linear packet reservoir with
at least

\[
                         {2W r^{1/4}\over8L}               \tag{2.3}
\]

packets, and all but

\[
 O\!\left(W\exp(-r^{1/8}/3)+Wr^{-3/16}\right)             \tag{2.4}
\]

of the owner/root resources have degree

\[
                         (1+o(1))r^{1/4}.                  \tag{2.5}
\]

#### Proof

Substitute (2.1)--(2.2) into Theorem 1.2.  The two error conditions are

\[
 \varepsilon^2\rho=r^{1/8},qquad
 {\rho\Xi\over\varepsilon}=O(r^{-3/16}).                 \tag{2.6}
\]

There are `N=2W` resource vertices.  `square`

This is the first integral reservoir statement which uses the stronger
aggregate collision mass rather than the false estimate
`binom(2L,2)Delta_2/D_0=Theta(1)`.

## 3. Deterministic anchored packet fans

The exact maximum codegree gives a different, fully deterministic
consequence.

### Theorem 3.1 (disjoint anchored fan)

Let `H` be `h`-uniform and `D`-regular with maximum pair codegree
`Delta_2`.  Let

\[
 A=\{v_1,\ldots,v_b\},\qquad Z\subseteq V(H)-A.           \tag{3.1}
\]

If

\[
       \bigl((b-1)(h+1)+|Z|\bigr)\Delta_2<D,              \tag{3.2}
\]

then there are pairwise disjoint packets `e_1,...,e_b` such that

\[
              e_i\cap A=\{v_i\},\qquad e_i\cap Z=\varnothing.
                                                                    \tag{3.3}
\]

#### Proof

Choose the packets in order.  Through `v_i` there are `D` candidates.
At most `(b-1)Delta_2` candidates contain another anchor, and at most
`|Z|Delta_2` meet `Z`.  For every previously selected packet `e_j`, at
most

\[
       \sum_{y\in e_j}d_H(v_i,y)\le h\Delta_2             \tag{3.4}
\]

candidates meet `e_j`; the induction invariant ensures `v_i notin e_j`.
The total number excluded is at most the left side of (3.2), so one
candidate remains.  `square`

### Corollary 3.2 (sqrt-r many private packet sockets)

For the parity-unified packet hypergraph, `Delta_2=2D_0/r`.  Hence the
anchored fan exists whenever

\[
                         2((b-1)(2L+1)+|Z|)<r.             \tag{3.5}
\]

In particular, with a fixed forbidden bank, one may prescribe

\[
                         b=\Theta(r/L)=\Theta(\sqrt r)     \tag{3.6}
\]

resource anchors and plant mutually private packet sockets through all of
them.

The fixed-size opposed-hinge clique bank may be planted first and entered
in `Z`.  Corollary 3.2 then plants any fixed packet bank disjoint from its
owner/root resources.  Thus the packet reservoir and the already-proved
Boolean `C6` attachment router coexist at bounded scale.  This is a
coexistence theorem, not yet an absorbing trade between the two banks.

## 4. The named-target spread and its exact contraction warning

Let `mathcal O` be one symmetric orbit of pure pull packets.  Let `a_s` be
the number of listed rank-`s` proper-window targets in one packet, and let
`a_(s,t,u)` be the number of ordered listed pairs `(S,T)` with

\[
                         |S|=s,\quad |T|=t,\quad|S\cap T|=u.\tag{4.1}
\]

Every packet's complete proper-window list is simple: intersection with
its private phase set recovers the cyclic interval, hence its width and
start.

### Proposition 4.1 (exact symmetric pair spread)

After uniform ground-set symmetrization,

\[
 {d(S,T)\over d(S)}
 = {a_{s,t,u}/a_s
    \over \binom su\binom{k-s}{t-u}}.                     \tag{4.2}
\]

For a pure `(delta,j)` orbit, a fixed rank occurs at at most two source
widths.  Consequently

\[
                         {a_{s,t,u}\over a_s}\le2L\le6D.  \tag{4.3}
\]

If `T` is not contained in `S`, then, throughout the strict lower range,

\[
 {d(S,T)\over d(S)}
       \le {6D\over k-s}=O(D/r)=o(1).                     \tag{4.4}
\]

#### Proof

There are `binom(k,s)` possible first targets and

\[
 \binom{k}{u}\binom{k-u}{s-u}\binom{k-s}{t-u}            \tag{4.5}
\]

ordered target pairs with the data (4.1).  Double counting packet-pair
incidences and dividing the latter count by `binom(k,s)` gives (4.2).
For each occurrence of `S`, there are at most `2L` listed occurrences at
rank `t`, proving (4.3).  When `u<t<r` and `s<r`, one has
`1<=t-u<k-s`, so `binom(k-s,t-u)>=k-s`.  This proves (4.4).  `square`

The containment case `T subset S` is different: the second denominator in
(4.2) becomes one.  Nested suffix targets in one packet are deliberately
correlated, and their normalized codegree need not vanish.  Therefore an
integral theorem may not simply append every named target as an independent
resource and quote a generic small-codegree nibble.  It must contract a
whole nested chain ticket, or condition on that ticket before applying a
spread argument.

## 5. What the reservoir does and does not prove

The exact degree also identifies the natural endpoint of an unabsorbed
random-like cover-down.  In the parity-unified packet system,

\[
 D_0={1\over2}(r-1)_a(r)_D,\qquad
 h=2L=2(D+a).                                              \tag{5.1}
\]

If a residual resource set behaves like an independent set of density
`u`, the mean residual degree is `D_0u^(h-1)`.  Its unit-degree threshold
is therefore

\[
 u_*=D_0^{-1/(2L-1)}.                                     \tag{5.2}
\]

### Proposition 5.1 (the critical square-root density)

At triangular depth `D=Theta(sqrt r)` and `a in {1,2}`,

\[
                         u_*=(1+o(1))r^{-1/2}.             \tag{5.3}
\]

#### Proof

Since `D=o(r)`,

\[
 \log D_0=(D+a)\log r+O(D^2/r+1)
          =L\log r+O(1).                                  \tag{5.4}
\]

Divide by `2L-1`.  As `L` tends to infinity,

\[
 {L\over2L-1}=\tfrac12+o(1),\qquad
 {D^2/r+1\over2L-1}=o(1),                                 \tag{5.5}
\]

and exponentiate.  `square`

Thus the same `W/sqrt(r)` scale appears in three independent places:

* the packet uniformity is `Theta(sqrt r)`;
* aggregate-linear sampling permits `rho=o(sqrt r)`;
* a random-like residual packet degree dies at density
  `(1+o(1))/sqrt r`.

This does not prove that every matching must leave that much.  It says
that an ordinary unabsorbed nibble has no degree reserve below that scale.
A proof of bounded leave therefore needs a mesoscopic absorber or exact
design mechanism already active while the residual still has
`Theta(W/sqrt r)` resources; a merely bounded terminal switch bank cannot
bridge the whole random-greedy gap.

Theorem 1.2 removes all multiple packet intersections from a large,
almost-regular reservoir at an `o(1)` relative cost.  It is well suited to
planting a bounded or slowly growing collection of private switches.

It does **not** give a near-perfect matching.  Even in a linear reservoir,
the `hD` singleton-intersection neighbourhood of one packet is the dominant
conflict term.  A one-shot isolated-edge alteration at sampling rate
`Theta(1/(hD))` therefore selects only `Theta(N/h^2)` packets, whereas a
factor needs `N/h` packets.

There is also a sharp scale warning for an independently sampled universal
reservoir.  To make the elementary union bound for zero sampled degree at
all `N=2W` resources effective requires

\[
                         \rho\gtrsim\log N=\Theta(r),       \tag{5.6}
\]

whereas aggregate-linear alteration requires

\[
                         \rho\Xi=o(1),qquad
                         \rho=o(\sqrt r).                  \tag{5.7}
\]

Thus one sparse independent reservoir cannot simultaneously be globally
spanning and aggregate-linear by this method.  The correct use is
two-stage:

1. obtain a cover-down matching with a structured small leave;
2. reserve chain-contracted packet switches and route the terminal
   owner/root attachment difference through the Boolean `C6` portal bank.

The exact open theorem is now narrower: prove the cover-down in the
growing-uniformity packet hypergraph, or prove that its leave lies in the
bounded trade lattice generated by the anchored packet fans and the
terminal `C6` router.
