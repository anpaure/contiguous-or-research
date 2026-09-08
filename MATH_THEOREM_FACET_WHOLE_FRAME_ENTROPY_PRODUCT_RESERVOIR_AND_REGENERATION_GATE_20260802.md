# Whole prime-slope frames: entropy survives the required product reservoir

Date: 2026-08-02  
Status: unconditional distinct-frame count, exact product-residual identities,
and an unconditional one-bite theorem.  The `q^2`-bite conclusion is proved
under one explicit residual-spread hypothesis.  No frame packing or OR-word
upper bound is claimed.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1,\qquad W=\binom{k}{r},
\]

and work in the canonical range, so `q=Theta(sqrt(k))`.  Let `p` be the
Bertrand prime used by the prime-slope construction,

\[
 q/3-1<p<2q/3,\qquad s=q-p,\qquad m=(p-1)/2.
\]

Thus `p,s,m=Theta(q)`.  Regard the complete owner-and-named-target deck of
one prime-slope frame as one hyperedge.  Its exact size is

\[
 K=m(q^2-2q+2)=\Theta(q^3).                    \tag{0.1}
\]

The pointed-flag contraction has only polynomial degree `Theta(q^6)` and
dies under the product residual needed for repeated bites.  The whole-frame
catalogue behaves completely differently:

\[
 \boxed{\log D_s=\Theta(q^2\log q)}              \tag{0.2}
\]

at every resource rank `s` used by a frame.  Here `D_s` is the exact degree
of a fixed rank-`s` resource in the full permutation-invariant catalogue.

If every named resource is retained independently with probability

\[
 \rho\ge 1-\alpha/q
\]

for fixed `alpha`, then, conditional on a resource surviving, its expected
residual degree is exactly

\[
 D_s\rho^{K-1}
   =\exp(\Theta(q^2\log q)-O(q^2)).              \tag{0.3}
\]

This still tends to infinity superpolynomially.  Conditional expected
pair-codegree ratios are multiplied by only `rho^(-1)=1+O(1/q)`.
Consequently the elementary degree-volume obstruction that killed the
plain-flag iteration is absent for whole frames.

An unconditional isolated bite from any residual hypergraph with the
correct edge-to-maximum-degree ratio selects `Omega(W/q^5)` frames.  Hence
`Theta(q^2)` regenerated bites would select

\[
                    \Omega(W/q^3)                 \tag{0.4}
\]

pairwise resource-disjoint frames, exactly the input required by the local
prime-slope amplifier.

The missing theorem is now exact.  One must sparsify the whole-frame
catalogue, or control its random matching residual, so that the
edge-to-maximum-degree ratio remains `Omega(W/q^2)` for `Theta(q^2)` bites.
Product retention has this ratio in expectation, but expectation alone is
not simultaneous residual concentration.  Near-duplicate frames are the
remaining covariance gate.  The singleton transverse collision is fully
included as an ordinary one-vertex intersection; no collision-multiplicity
assumption is used below.

## 1. The simple whole-frame hypergraph

Let `H` be the simple hypergraph whose vertices are all actual owner and
named-target resources at the ranks used by a prime-slope frame, and whose
edges are the distinct complete resource decks of all such frames on
`[k]`.  All cores, field embeddings, private banks, legal gap placements,
and low labels are included.  Repeated descriptions of the same deck are
identified.

One edge has the exact rank inventory

\[
\begin{array}{c|c}
\text{rank}&\text{vertices in the edge}\\ \hline
r&mq,\\
c&m,\\
c+1&m,\\
c+j,\ 2\le j\le q-2&mq.
\end{array}                                             \tag{1.1}
\]

Summing (1.1) gives (0.1).  The symmetric group on `[k]` preserves the
catalogue and is transitive on each rank.  If `F=|E(H)|`, every vertex of a
fixed rank `u` therefore has exact degree

\[
             D_u={F R_u\over \binom{k}{u}},             \tag{1.2}
\]

where `R_u` is the corresponding entry of (1.1).

All ranks in (1.1) are within `q=Theta(sqrt(k))` of the middle.  Hence,
uniformly over them,

\[
       \binom{k}{u}=\Theta(W),\qquad
       m\le R_u\le mq=\Theta(q^2).                       \tag{1.3}
\]

The constants in `Theta(W)` may depend only on the fixed canonical
asymptotic window, not on `u` or `k`.

## 2. There are `exp(Theta(q^2 log q))` distinct decks

### Theorem 2.1 (whole-frame entropy)

For the simple catalogue `H`,

\[
                 \log F=\Theta(q^2\log q).              \tag{2.1}
\]

Consequently (0.2) holds at every rank in (1.1).

### Proof

The upper bound is immediate: a frame uses `O(q^2)` coordinate roles, each
chosen from a `k=Theta(q^2)` element set, together with at most
`exp(O(q^2 log q))` order data.

For the lower bound, fix one core `C` and one field pool `I`.  Let

\[
 n=k-c-p.
\]

The coordinate-budget proof for prime-slope frames leaves a fixed positive
fraction of the `Theta(q^2)` outside coordinates unused.  In particular,
for some absolute `eta>0` and all sufficiently large `q`, throughout the
successive choice of the `m` private `s`-sets there remain at least
`eta q^2` available coordinates.

The number of ordered disjoint private-bank systems is therefore at least

\[
             \binom{\eta q^2}{s}^{m}
       \ge (\eta q^2/s)^{sm}
       =\exp(\Theta(q^2\log q)).                         \tag{2.2}
\]

Fix a deterministic legal placement rule inside each chosen bank: two
distinguished private tags occupy two fixed nonadjacent field gaps, and the
remaining private tags are inserted in a fixed order.  This loses no factor
from (2.2).

It remains to check that (2.2) is not merely a count of descriptions.  In
one module, its `q` owners are the facets

\[
              C\cup(I\cup X_a-\{v\}),\qquad v\in I\cup X_a.
\]

Two distinct owners of this module have union of rank `r+1`.  Owners from
two different private banks have union of rank at least

\[
 c+p+2s-2=r+s-1>r+1                                  \tag{2.3}
\]

for all sufficiently large `q`.  Thus the graph on a frame's owners in
which two owners are adjacent when their union has rank `r+1` recovers the
individual module blocks as its maximal cliques.  The union of a recovered
block gives `C union I union X_a`; intersecting all owners in that block
gives `C`.  Intersecting the recovered tag sets over all blocks gives `I`,
and hence every private bank `X_a` is recovered.

Only the permutation of the `m` recovered blocks can forget their original
slope labels.  Dividing (2.2) by `m!` therefore gives a lower bound for
distinct resource decks.  Since

\[
                         \log(m!)=O(q\log q)=o(q^2\log q),
\]

the lower exponent in (2.1) follows.

Finally, (1.2)--(1.3) and `log W=Theta(k)=Theta(q^2)` show

\[
 \log D_u=\log F-O(q^2)=\Theta(q^2\log q),
\]

uniformly over all used ranks.  \(\square\)

## 3. Exact product-residual identities

Let `U` retain every resource vertex independently with probability `rho`,
and write `H[U]` for the induced frame catalogue.

### Proposition 3.1 (product degree and codegree)

For a rank-`u` resource `x`, conditional on `x in U`,

\[
        \mathbb E[d_{H[U]}(x)\mid x\in U]
                  =D_u\rho^{K-1}.                         \tag{3.1}
\]

For distinct resources `x,y`, conditional on both surviving,

\[
 \mathbb E[d_{H[U]}(x,y)\mid x,y\in U]
                  =d_H(x,y)\rho^{K-2}.                    \tag{3.2}
\]

Also

\[
                  \mathbb E|E(H[U])|=F\rho^K.            \tag{3.3}
\]

Thus the ratio of the two conditional expectations in (3.2) and (3.1)
is exactly

\[
 {1\over\rho}{d_H(x,y)\over D_u}.                        \tag{3.4}
\]

### Proof

Every edge through `x` survives precisely when its other `K-1` vertices
survive.  Linearity of expectation gives (3.1).  The same argument leaves
`K-2` unconditioned vertices for an edge through `x,y`, proving (3.2).
Equation (3.3) is identical with no conditioned vertex.  Division gives
(3.4).  No independence between different frame-survival events is being
asserted or used. \(\square\)

### Corollary 3.2 (the `q^2`-round entropy test passes)

For fixed `alpha>0` and `rho>=1-alpha/q`,

\[
 \begin{aligned}
 \log(D_u\rho^{K-1})
   &=\Theta(q^2\log q)-O(q^2),\\
 \rho^{-1}&=1+O(1/q).
 \end{aligned}                                           \tag{3.5}
\]

In particular the expected product-residual degrees tend to infinity as
`exp(Theta(q^2 log q))`.

### Proof

Use `K=Theta(q^3)` and

\[
               \log\rho=-O(1/q).
\]

Then `(K-1)log rho=-O(q^2)`, while Theorem 2.1 gives the larger positive
term `Theta(q^2 log q)`.  The second row is the geometric expansion of
`1/rho`. \(\square\)

This is the precise contrast with the pointed-flag degree
`D=Theta(q^6)`: there `D exp(-Theta(q))=o(1)` after only `Theta(q)`
product-like bites.  Whole frames retain a `log q` factor in the exponent
after the `Theta(q^2)` bites they require.

## 4. An unconditional isolated bite

### Lemma 4.1 (maximum-degree bite)

Let `G` be any simple `K`-uniform hypergraph with `E` edges and maximum
vertex degree `Delta`.  If `K Delta>=2`, then `G` has a matching of size at
least

\[
                         {E\over4K\Delta}.                \tag{4.1}
\]

### Proof

Mark each edge independently with probability `p=1/(K Delta)` and retain a
marked edge if no other marked edge intersects it.  An edge meets at most
`K Delta-1` other edges.  Hence its retention probability is at least

\[
 p(1-p)^{K\Delta-1}\ge {1\over4K\Delta}.
\]

The retained edges form a matching, and their expected number is at least
the right side of (4.1).  Some outcome attains the expectation. \(\square\)

### Corollary 4.2 (one whole-frame bite)

The full frame catalogue contains a matching of

\[
                         \Omega(W/q^5)                    \tag{4.2}
\]

whole prime-slope frames.

### Proof

Equations (1.2)--(1.3) give

\[
                 \Delta=\Theta(Fq^2/W).
\]

Substitute this and `K=Theta(q^3)` into (4.1). \(\square\)

This recovers only the ordinary one-bite scale.  Its purpose here is to
make the exact iteration count transparent.

## 5. The exact regeneration criterion

### Theorem 5.1 (edge/degree regeneration suffices)

Suppose a serial sequence of residual whole-frame catalogues `H_t` exists
for `0<=t<T`, where each next residual deletes the resources used by the
matching selected at stage `t`, and suppose

\[
 T=\theta q^2,
 \qquad
 { |E(H_t)|\over \Delta(H_t)}\ge\kappa {W\over q^2}       \tag{5.1}
\]

for fixed positive `theta,kappa`.  Then their union contains

\[
                         \Omega(W/q^3)                    \tag{5.2}
\]

pairwise resource-disjoint prime-slope frames.

### Proof

Lemma 4.1 applied at stage `t` supplies at least

\[
 {1\over4K}{|E(H_t)|\over\Delta(H_t)}
       =\Omega(W/q^5)
\]

frames.  Later stages use only uncovered resources, so all bites are
mutually disjoint.  Summing over `Theta(q^2)` stages proves (5.2). \(\square\)

The total consumed resource volume in this conclusion is `Theta(W)`, only
a `Theta(1/q)` fraction of the `Theta(qW)` resources across the relevant
ranks.  Thus (5.1) asks for no scalar overpacking.

Product retention has the correct ratio at the level of expectations.  By
(3.1)--(3.3),

\[
 {\mathbb E|E(H[U])|\over
   \max_u\mathbb E[d_{H[U]}(u)\mid u\in U]}
       =\Theta(\rho W/q^2).                              \tag{5.3}
\]

What is not proved is that one outcome, and then the actual matching
residuals of `Theta(q^2)` successive outcomes, satisfy the simultaneous
analogue of (5.3).

## 6. A proof-safe sparsification target

For a subcatalogue `S` and `0<rho<1`, define the product cluster energies

\[
 \begin{aligned}
 \mathcal C(S;\rho)
 &= {1\over |S|^2}
    \sum_{E\ne F\in S}\left(\rho^{-|E\cap F|}-1\right),\\
 \mathcal C_x(S;\rho)
 &= {1\over d_S(x)^2}
    \sum_{\substack{E\ne F\in S\\x\in E\cap F}}
       \left(\rho^{-(|E\cap F|-1)}-1\right).
                                                               \tag{6.1}
 \end{aligned}
\]

These are the exact normalized covariance sums for the product edge count
and the product degree at `x`.  The second-moment identities are

\[
 {\operatorname{Var}|E(S[U])|\over
    (\mathbb E|E(S[U])|)^2}
 \le {1\over |S|\rho^K}+\mathcal C(S;\rho),              \tag{6.2}
\]

and, conditional on `x in U`,

\[
 {\operatorname{Var}d_{S[U]}(x)\over
    (\mathbb E d_{S[U]}(x))^2}
 \le {1\over d_S(x)\rho^{K-1}}+\mathcal C_x(S;\rho).     \tag{6.3}
\]

They follow by expanding the two squares and using

\[
 \Pr(E,F\subseteq U)=\rho^{2K-|E\cap F|}.
\]

Therefore a sufficient two-stage theorem is now concrete:

> **Whole-frame reservoir sparsification.**  Find a rank-balanced
> subcatalogue `S` with the same `exp(Theta(q^2 log q))` degree scale and,
> uniformly for `rho>=1-alpha/q`, product cluster energies small enough to
> make (6.2)--(6.3) simultaneous over all `exp(O(q^2))` named resources and
> stable under the selected bites.

The entropy margin in Corollary 3.2 is large enough for exponentially
strong concentration if such a cluster bound is proved.  It is not itself
a cluster bound.  Frames differing in only a small part of their private
bank data can share many resources, so blindly invoking Chernoff or a
fixed-uniformity nibble here would be invalid.

The singleton transverse construction causes terms with `|E cap F|=1` in
(6.1).  At `rho=1-O(1/q)` each such factor is only
`rho^(-1)-1=O(1/q)`.  Hence singleton collisions are not ignored and do not
by themselves threaten product concentration.  The dangerous class is the
near-duplicate tail with large `|E cap F|`; it is precisely what the
sparsification theorem must control.

## 7. Scope

The following are proved here:

1. the simple whole-frame catalogue has degree
   `exp(Theta(q^2 log q))` at every used rank;
2. its product-residual expected degrees survive density `1-Theta(1/q)`;
3. normalized expected pair ratios change by only `1+O(1/q)`;
4. one whole-frame bite gives `Omega(W/q^5)` frames;
5. the single deterministic ratio (5.1) through `Theta(q^2)` bites would
   prove the desired `Omega(W/q^3)` frame packing.

The following are not proved:

* a subcatalogue satisfying the cluster-energy target;
* simultaneous product concentration over all resources;
* transfer from product residuals to actual matching residuals;
* allocation of primitive and short-buffer source occurrences;
* component fusion, upper shadows, residence, pins, or compiler closure.

Thus this note removes the **degree exhaustion** objection to a whole-frame
iteration but leaves a sharply stated **correlated residual concentration**
theorem.  It neither assumes collision clustering nor claims the global
frame packing.

## 8. Dependencies

The local frame and exact resource ledger are in
`MATH_THEOREM_FACET_PRIME_SLOPE_FRAME_Q_AMPLIFIER_20260802.md`.
The failure of the polynomial pointed-flag iteration is in
`MATH_AUDIT_FACET_POINTED_FLAG_GROWING_NIBBLE_AND_CONFLICT_BARRIER_20260802.md`.
The literal singleton transverse collision is in
`MATH_OBSTRUCTION_FACET_PRIME_SLOPE_SINGLETON_TRANSVERSE_COLLISION_20260802.md`.

