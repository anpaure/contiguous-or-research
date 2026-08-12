# Endpoint-triangular bounded chains: exact fractional feasibility and the integral gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It sharpens the
architecture-free endpoint-chain condition, solves its complete fractional
relaxation, identifies every rank/Greene--Kleitman cut, and gives a perfect-
graph counterexample to automatic integral rounding.  It does **not** prove an
integral bounded-chain partition of the Boolean lower ideal and makes no owner
or word-serialization claim.

## 0. Setup and verdict

Put

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|.
\]

Let `d=d(k)` be the least nonnegative integer satisfying

\[
 dW+{d+1\choose2}\ge\Lambda.                         \tag{0.1}
\]

Suppose `h>=1` and a universal word has length

\[
 n=W+h,\qquad h=d+C,\qquad C\ge0.                    \tag{0.2}
\]

The architecture-free endpoint theorem says that every strict-lower target
has a witnessing interval of length at most `h`.  Remembering the left
boundary gives the following strictly sharper necessary condition:

\[
 \boxed{
 \mathcal L\text{ must partition into }n\text{ chains with capacities }
 (\underbrace{h,\ldots,h}_{W+1},h-1,h-2,\ldots,1).}
                                                               \tag{0.3}
\]

Here the capacities are written in decreasing order.  The total capacity is

\[
 hW+{h+1\choose2}.                                    \tag{0.4}
\]

The main positive theorem is that (0.3) is always feasible **fractionally**,
with every named Boolean target covered exactly once.  Equivalently, all
rank-slot max-flow cuts pass.  All generalized Greene--Kleitman cuts pass as
well, and their worst members are the unions of the top `t` Boolean ranks.

For the simpler uniform capacity `h`, the exact fractional minimum chain mass
is

\[
 \boxed{
 \kappa_h^*(\mathcal L)
 =\max\left\{\max_{1\le s<r}{k\choose s},\ {\Lambda\over h}\right\}.}
                                                               \tag{0.5}
\]

At exact length `B(k)=W+d`, this leaves at least `(d-1)/2` units of
fractional chain-mass slack.

None of this implies an integral partition.  A family of complete
multipartite (hence perfect) incomparability graphs has all the same
Greene--Kleitman inequalities and a feasible fractional triangular-slot
cover in `n` slots, but needs `n+1` integral bounded chains.  Thus perfectness,
rank counts, strong Sperner, and the full fractional slot flow do not provide
the missing Boolean rounding theorem.

## 1. The exact endpoint capacity vector

Let `A=(A_1,...,A_n)` be universal and choose one witness interval for every
rank-`r` target.  The standard ordered-middle-witness argument shows that
every interval representing a target in `mathcal L` has length at most

\[
                         n-W=h.                       \tag{1.1}
\]

Choose one such interval for every lower target and group targets by their
right endpoint.  At a fixed endpoint `j`, the represented values are nested,
so they form a chain.  The possible interval lengths are

\[
                         1,2,\ldots,\min(h,j).         \tag{1.2}
\]

Consequently the chain at endpoint `j` has capacity

\[
                         c_j=\min(h,j).                \tag{1.3}
\]

There are `h-1` clipped capacities `1,...,h-1`, followed by

\[
 n-h+1=(W+h)-h+1=W+1
\]

copies of `h`.  This proves (0.3).  Summing gives

\[
 \sum_{j=1}^n c_j
 =h(W+1)+{h(h-1)\over2}
 =hW+{h+1\choose2},                                  \tag{1.4}
\]

which is (0.4).

The exact endpoint vacancy is therefore

\[
 V_C^\triangle
 =hW+{h+1\choose2}-\Lambda.                          \tag{1.5}
\]

If

\[
 \sigma=dW+{d+1\choose2}-\Lambda,
\]

then

\[
 V_C^\triangle
 =\sigma+CW+Cd+{C(C+1)\over2}.                       \tag{1.6}
\]

Minimality of `d` gives `0<=sigma<W+d`, so the average vacancy remains
strictly below `C+1+o(1)`.  Formula (1.5), rather than the rectangular
capacity `hn`, is the exact static shadow of the left boundary.

## 2. Every Greene--Kleitman cut passes

For a finite poset `P`, let `a_t(P)` be the maximum cardinality of a union
of `t` antichains.  If `P` is partitioned into chains of capacities
`c_1,...,c_n`, then necessarily

\[
 a_t(P)\le\sum_{j=1}^n\min(t,c_j)                    \tag{2.1}
\]

for every `t`: each chain contributes at most `t` elements to a union of
`t` antichains and at most its own capacity.

For the endpoint vector (0.3), direct summation gives, for `1<=t<=h`,

\[
 \sum_{j=1}^n\min(t,c_j)
 =t(W+h)-{t\choose2}.                                \tag{2.2}
\]

For `t>=h` the right side of (2.1) is the total capacity (1.4).

The Boolean lattice is strongly Sperner.  Since the strict-lower rank
numbers increase toward rank `r-1`,

\[
 a_t(\mathcal L)
 =\sum_{i=1}^{\min(t,r-1)}{k\choose r-i}.             \tag{2.3}
\]

In particular, when `t<=h`,

\[
 a_t(\mathcal L)\le tW
 \le t(W+h)-{t\choose2},                             \tag{2.4}
\]

and for `t>=h`,

\[
 a_t(\mathcal L)\le\Lambda
 \le dW+{d+1\choose2}
 \le hW+{h+1\choose2}.                              \tag{2.5}
\]

Thus every cut (2.1) passes.  The exact Boolean rank-cut margins for
`t<=h` are

\[
 \Delta_t
 =t(W+h)-{t\choose2}
  -\sum_{i=1}^t{k\choose r-i}\ge0.                  \tag{2.6}
\]

This proves that generalized Dilworth/Greene--Kleitman inequalities cannot
be the missing endpoint-chain obstruction.

## 3. Exact uniform-cap fractional minimum

Let `\mathfrak C_h(P)` be the chains of `P` having at most `h` elements.  The
fractional bounded-chain cover number is

\[
 \kappa_h^*(P)=
 \min\left\{\sum_{C\in\mathfrak C_h(P)}x_C:
 x_C\ge0,\ \sum_{C\ni v}x_C\ge1\ (v\in P)\right\}. \tag{3.1}
\]

### Theorem 3.1

For the complete strict Boolean lower ideal, equation (0.5) holds.

### Proof

Put

\[
 M=\max_{1\le s<r}{k\choose s}={k\choose r-1}.
\]

Every chain meets a fixed rank at most once, so summing the cover constraints
over that rank gives `kappa_h^*>=M`.  Every chain has at most `h` elements,
so summing over all targets gives `kappa_h^*>=Lambda/h`.

Conversely, put

\[
 q=\max\{M,\Lambda/h\},\qquad
 p_s={\binom{k}{s}\over q}\quad(1\le s<r).          \tag{3.2}
\]

Then `0<=p_s<=1` and `sum_s p_s<=h`.  Hence `p` lies in the independent-set
polytope of the uniform matroid `U_(h,r-1)`, so it is a convex combination
of incidence vectors of rank sets

\[
 R\subseteq\{1,\ldots,r-1\},\qquad |R|\le h.         \tag{3.3}
\]

For one such `R`, choose a uniformly random permutation `pi` of `[k]` and
take the nested flag

\[
 \{\pi_1,\ldots,\pi_s\}\qquad(s\in R).              \tag{3.4}
\]

A fixed rank-`s` target appears with probability `1/binom(k,s)`, conditional
on `s in R`.  Multiplying this random-chain distribution by total mass `q`
therefore gives every rank-`s` target mass

\[
 q\,{p_s\over\binom{k}{s}}=1.                        \tag{3.5}
\]

The total chain mass is `q`, proving the upper bound and the theorem.
\(\square\)

Assume `d>=1`.  At `h=d`, write

\[
 \sigma=dW+{d+1\choose2}-\Lambda\ge0.
\]

Then

\[
 {\Lambda\over d}
 =W+{d+1\over2}-{\sigma\over d},                    \tag{3.6}
\]

while `M<=W`.  Consequently

\[
 \kappa_d^*(\mathcal L)\le W+{d+1\over2},
 \qquad
 (W+d)-\kappa_d^*(\mathcal L)\ge{d-1\over2}.        \tag{3.7}
\]

So exact-`B` endpoint chainization has `Theta(d)` fractional chain-mass
reserve; its obstruction, if any, is integral and Boolean-geometric.

## 4. Exact fractional realization of the triangular slots

The preceding theorem does not remember the clipped slots.  They too admit
an exact fractional solution.

### Theorem 4.1 (fractional endpoint-triangular factor)

For every `h>=d`, there is a fractional selection of one chain in each of
the `n=W+h` labelled endpoint slots, with slot `j` using at most `c_j`
targets, such that every member of `mathcal L` has total incidence exactly
one.

### Proof

First solve the rank-to-slot transportation problem.  We seek numbers
`p_(j,s)` satisfying

\[
 0\le p_{j,s}\le1,\qquad
 \sum_jp_{j,s}={k\choose s},\qquad
 \sum_sp_{j,s}\le c_j.                              \tag{4.1}
\]

This is a bipartite `b`-matching.  Its max-flow cuts are

\[
 \sum_{s\in R}{k\choose s}
 \le\sum_{j=1}^n\min(c_j,|R|)                       \tag{4.2}
\]

for every set `R` of ranks.  For fixed `|R|=t`, the left side is maximized
by the top `t` strict-lower ranks.  Equations (2.2)--(2.5) prove every cut,
so (4.1) has a solution.

For each slot `j`, the vector `(p_(j,s))_s` lies in the independent-set
polytope of the uniform matroid of rank `c_j`.  Decompose it into rank
patterns of size at most `c_j`; add the empty pattern so the coefficients
sum to one.  Conditional on a pattern, use the uniform random flag (3.4).
For a fixed rank-`s` target, the total incidence over all slots is

\[
 \sum_j{p_{j,s}\over\binom{k}{s}}=1.                \tag{4.3}
\]

This is the required fractional labelled-slot factor. \(\square\)

Thus the complete rank-slot flow, not just its rank-count relaxation, is
integral at the rank-pattern level and exactly realizable by fractional
named Boolean flags.  The unsolved step is choosing one literal flag in
every slot with no repeated named target.

## 5. Perfectness and all cut inequalities still do not round

The next example proves that no generic perfect-graph or Greene--Kleitman
rounding theorem can close Theorem 4.1.

### Proposition 5.1 (fractional triangular slots, integral failure)

Fix `h>=2` and `n>=h+2`.  Let `P_(n,h)` be the disjoint union of

* `n-3` one-element chains; and
* two chains, each having `h+1` elements.

Give `n` slots the triangular capacities

\[
 (\underbrace{h,\ldots,h}_{n-h+1},h-1,\ldots,1).    \tag{5.1}
\]

Then:

1. every Greene--Kleitman capacity inequality (2.1) holds;
2. a fractional labelled-slot cover exists;
3. no integral cover in the `n` slots exists; in fact `n+1` bounded chains
   are necessary and sufficient; and
4. the incomparability graph is complete multipartite and hence perfect.

### Proof

Elements in different order components are incomparable, so every chain is
contained in one component.  Each singleton component needs one chain and
each `(h+1)`-chain needs two chains of capacity at most `h`.  Thus the
integral minimum is

\[
                         (n-3)+2+2=n+1.              \tag{5.2}
\]

For the fractional cover of one `(h+1)`-chain, take its `h+1` subchains
obtained by omitting one element, each with weight `1/h`.  Every element
then has weight one and the total chain mass is `(h+1)/h`.  The two long
components therefore need total mass

\[
                         2+{2\over h}\le3.           \tag{5.3}
\]

Assign the `n-3` singleton components to `n-3` slots, leaving three
capacity-`h` slots; these exist because `n>=h+2`.  Distribute the
`2h+2<=3h` equal atoms of weight `1/h` from (5.3) among those three slots
and fill unused mass by the empty chain.  This proves fractional labelled-
slot feasibility.

The largest union of `t` antichains has size

\[
 a_t(P_{n,h})=n-3+2\min(t,h+1).                     \tag{5.4}
\]

For `t=1`, this is `n-1<=n`.  For `2<=t<=h`, using `n>=t+2`,

\[
 \begin{aligned}
 t n-{t\choose2}-a_t(P_{n,h})
 &=(t-1)n-{t(t-1)\over2}-2t+3\\
 &\ge {t^2-t+2\over2}>0.                            \tag{5.5}
 \end{aligned}
\]

For `t>=h`, the right side of (2.1) is the total capacity
`\(hn-\binom h2\)`, which is at least

\[
 |P_{n,h}|=n+2h-1                                   \tag{5.6}
\]

when `n>=h+2`.  Hence all Greene--Kleitman cuts pass.

Finally, the incomparability graph of a disjoint union of chains is the
complete multipartite graph whose parts are those chains.  Complete
multipartite graphs are perfect.  Its bounded color classes nevertheless
cannot mix parts, giving exactly the integral count (5.2). \(\square\)

This example has a genuine fractional-to-integral gap while satisfying the
same triangular capacity profile.  It does not disprove Boolean integral
chainization; it proves that a positive theorem must exploit Boolean
exchange geometry beyond perfectness and all rank/Greene--Kleitman cuts.

## 6. Exact surviving integral problem

For any poset `P`, let

\[
 \kappa_h(P)=
 \min\left\{\sum_{C\in\mathfrak C_h(P)}x_C:
 x_C\in\{0,1\},\ \sum_{C\ni v}x_C\ge1\ (v\in P)\right\}. \tag{6.1}
\]

A cover can be turned into a partition by assigning every element to one
chosen containing chain and deleting it from the others.  Thus (6.1) is
exactly the minimum number of chains of cardinality at most `h` in a
partition of `P`.  In graph language it is the bounded chromatic number of
the incomparability graph, with every color class capped by `h`.

The endpoint-triangular version is the analogous configuration problem with
one chain selected in each labelled slot of capacity `c_j`.  Theorem 4.1
solves its fractional relaxation for `mathcal L`.  Proposition 5.1 shows
that the integral relaxation is not a consequence of perfect graph
integrality.

Accordingly, the honest abstract frontier is

\[
 \boxed{
 \text{Does }\mathcal L\text{ admit the integral endpoint-triangular
 partition (0.3) for }h=d+C?}                       \tag{6.2}
\]

Even a positive answer to (6.2) is only the first gate.  It does not give:

1. **distinct middle-owner containment:** the `W` central owner occurrences
   and the `h` boundary chains must be correlated with the selected rank-`r`
   witness band;
2. **the left-endpoint system:** one word simultaneously induces a second
   nested family from intervals with fixed left endpoint;
3. **countdown serialization:** neighboring endpoint chains share source
   letters, so their successive differences must satisfy one common
   suffix-OR cocycle; or
4. **residence, upper shadows, topology, and common-cap compatibility.**

The complete implication chain is therefore

\[
 \boxed{
 \text{fractional endpoint-triangular chains (proved)}
 \longrightarrow
 \text{integral Boolean bounded coloring (open)}
 \longrightarrow
 \text{owner correlation (open)}
 \longrightarrow
 \text{two-sided countdown serialization (open).}}
\]
