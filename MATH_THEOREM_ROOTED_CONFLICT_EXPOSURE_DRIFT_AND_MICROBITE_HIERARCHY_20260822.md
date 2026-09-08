# Rooted conflict exposure: the exact adaptive microbite hierarchy

**Date:** 2026-08-22  
**Status:** unconditional reduction and cap-only counterexample; the
punctured Gate A comparison remains open

The fixed-slice theorem shows that exact shore sizes are harmless.  This
note identifies the first genuinely history-dependent statistic.  In an
arbitrary current residual hypergraph, the conditional drift of a target's
degree is determined by the average conflict exposure of configurations
through that target.  Degrees alone do not determine this exposure.

The result has three parts.

1. An exact derivative and a uniform microbite expansion identify the
   rooted exposure discrepancy controlling normalized degree drift.
2. The same calculation gives a finite factorial-moment hierarchy through
   every fixed order; order six is the hierarchy relevant to the current
   bad-incidence proof.
3. A completely regular 3-uniform example has maximum/average degree ratio
   one but two different rooted exposure drifts.  With positive probability
   one isolated-edge bite raises the ratio to two.  Thus no theorem based
   only on the current degree cap can prove Gate A.

No comparison of full residual-state laws is used.

## 1. General isolated-edge bite

Let `H` be a finite simple hypergraph.  Its vertex set may be partitioned
into shores `V_sigma`, and every edge contains exactly `k_sigma` vertices
of shore `sigma`.  Write

\[
 Z=|E(H)|,\qquad d(v)=|\{F:v\in F\}|,\qquad
 \bar d_\sigma={k_\sigma Z\over |V_\sigma|}.          \tag{1.1}
\]

For an edge `F`, let

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad
 C_F=|\Gamma(F)|,qquad
 \Delta_C=\max_F C_F.                                 \tag{1.2}
\]

Thus `Gamma(F)` is the closed conflict neighbourhood.  Put

\[
                         \overline C={1\over Z}\sum_FC_F. \tag{1.3}
\]

Independently mark every edge with probability `p`.  Accept a marked edge
when it has no other marked neighbour, delete every vertex of every
accepted edge, and let `H_p` be the residual induced hypergraph.  Undeleted
vertices remain in their shores even if their residual degree is zero.
Accepted edges are pairwise disjoint.

Whenever a random variable such as `d_(H_p)(v)` is written for an original
target which may be deleted, its value is defined to be zero on deletion.
With this convention
`E d_(H_p)(v)=Pr(v survives) E[d_(H_p)(v) | v survives]` literally.

For a target `v` with positive degree define

\[
 A_v={1\over d(v)}\sum_{F\ni v}C_F,\qquad
 E_v=A_v-d(v),                                        \tag{1.4}
\]

and its shore-normalized exposure discrepancy

\[
 \boxed{
 \Xi_v=E_v-(\overline C-\bar d_\sigma),qquad v\in V_\sigma.
 }                                                     \tag{1.5}
\]

## 2. Exact tangent identity

Let

\[
 s_v(p)=\Pr(v\text{ survives}),qquad
 M_v(p)=\mathbb E[d_{H_p}(v)\mid v\text{ survives}].  \tag{2.1}
\]

Define the annealed empirical scale

\[
 \bar d_\sigma^{\rm ann}(p)
 ={k_\sigma\mathbb E|E(H_p)|
       \over\mathbb E|V_\sigma(H_p)|}.                \tag{2.2}
\]

### Theorem 2.1 (rooted exposure drift)

At `p=0`,

\[
 s_v'(0)=-d(v),                                       \tag{2.3}
\]

\[
 {d\over dp}\log M_v(p)\bigg|_{p=0}=-E_v,           \tag{2.4}
\]

\[
 {d\over dp}\log\bar d_\sigma^{\rm ann}(p)
       \bigg|_{p=0}=-(\overline C-\bar d_\sigma),     \tag{2.5}
\]

and consequently

\[
 \boxed{
 {d\over dp}\log {M_v(p)\over\bar d_\sigma^{\rm ann}(p)}
       \bigg|_{p=0}=-\Xi_v.}                         \tag{2.6}
\]

#### Proof

To first order exactly one edge is marked, and that edge is automatically
accepted.  Target `v` is deleted for precisely the `d(v)` single marks on
its star, proving (2.3).

For `F\ni v`, the configuration `F` survives precisely when no accepted
edge meets it.  A single marked edge destroys `F` exactly when it belongs
to `Gamma(F)`.  Therefore

\[
 {d\over dp}\mathbb E d_{H_p}(v)\bigg|_{p=0}
 =-\sum_{F\ni v}C_F=-d(v)A_v.                       \tag{2.7}
\]

Since
`E d_(H_p)(v)=s_v(p)M_v(p)`, logarithmic differentiation of (2.7)
and (2.3) gives (2.4).

Similarly,

\[
 {d\over dp}\mathbb E|E(H_p)|\bigg|_{p=0}
 =-\sum_FC_F=-Z\overline C.                         \tag{2.8}
\]

One accepted edge removes exactly `k_sigma` targets from shore `sigma`, so

\[
 {d\over dp}\mathbb E|V_\sigma(H_p)|\bigg|_{p=0}
 =-k_\sigma Z=-|V_\sigma|\bar d_\sigma.             \tag{2.9}
\]

Equations (2.8)--(2.9) prove (2.5), and subtraction proves (2.6).
\(\square\)

Thus `Xi_v<0` means that, conditional on surviving the bite, target `v`
is enriched relative to its shore's empirical degree scale.

## 3. Uniform finite-microbite expansion

The tangent calculation has a uniform remainder which uses no independence
assumption on the current residual.

### Lemma 3.1 (one local union)

Let \(\mathcal A\) be a set of edges and put

\[
                         C(\mathcal A)=
                  \left|\bigcup_{F\in\mathcal A}\Gamma(F)\right|. \tag{3.1}
\]

For fixed \(\ell=|\mathcal A|\) and \(p\Delta_C\le1/4\),

\[
 \Pr(\text{every }F\in\mathcal A\text{ survives})
 =1-pC(\mathcal A)+O_\ell(p^2\Delta_C^2).            \tag{3.2}
\]

#### Proof

Let \(U=\bigcup_{F\in\mathcal A}\Gamma(F)\).  If no edge of \(U\) is marked,
every member of \(\mathcal A\) survives.  If an edge of \(U\) is marked but no
accepted edge lies in `U`, then some marked edge `e in U` has a marked
conflict neighbour.  By a union bound, this exceptional event has
probability at most

\[
 p^2\sum_{e\in U}(C_e-1)
 \le p^2|U|\Delta_C=O_\ell(p^2\Delta_C^2).           \tag{3.3}
\]

Also

\[
 \Pr(U\text{ contains a mark})
 =1-(1-p)^{|U|}=p|U|+O(p^2|U|^2).                    \tag{3.4}
\]

Since `|U|<=ell Delta_C`, (3.2) follows.
\(\square\)

### Theorem 3.2 (finite rooted drift)

Uniformly for `p Delta_C<=1/4`,

\[
 {M_v(p)\over d(v)}
 =1-pE_v+O(p^2\Delta_C^2),                           \tag{3.5}
\]

\[
 {\bar d_\sigma^{\rm ann}(p)\over\bar d_\sigma}
 =1-p(\overline C-\bar d_\sigma)
       +O(p^2\Delta_C^2),                            \tag{3.6}
\]

and hence

\[
 \boxed{
 {M_v(p)/\bar d_\sigma^{\rm ann}(p)
       \over d(v)/\bar d_\sigma}
 =1-p\Xi_v+O(p^2\Delta_C^2).}                       \tag{3.7}
\]

#### Proof

Lemma 3.1 with \(\mathcal A=\{F\}\) gives

\[
 \mathbb E d_{H_p}(v)
 =d(v)-p\sum_{F\ni v}C_F+O(p^2d(v)\Delta_C^2).       \tag{3.8}
\]

The same marked-star argument gives

\[
 s_v(p)=1-pd(v)+O(p^2d(v)\Delta_C).                  \tag{3.9}
\]

Divide (3.8) by (3.9) and use `d(v),A_v<=Delta_C` to
obtain (3.5).

Summing (3.2) over single configurations gives

\[
 {\mathbb E|E(H_p)|\over Z}
 =1-p\overline C+O(p^2\Delta_C^2).                  \tag{3.10}
\]

If `Y` is the number of accepted edges, then exactly

\[
 \mathbb EY=\sum_Fp(1-p)^{C_F-1}=pZ(1+O(p\Delta_C)). \tag{3.11}
\]

Since accepted edges are disjoint,
`|V_sigma(H_p)|=|V_sigma|-k_sigma Y`.  Divide its expectation by
`|V_sigma|` and use (1.1) to get

\[
 {\mathbb E|V_\sigma(H_p)|\over|V_\sigma|}
 =1-p\bar d_\sigma+O(p^2\bar d_\sigma\Delta_C).      \tag{3.12}
\]

Equations (3.10)--(3.12) prove (3.6).  Dividing (3.5) by (3.6) proves
(3.7).
\(\square\)

## 4. The factorial-moment hierarchy

For a positive integer `ell<=d(v)`, let `mathcal T_(ell,v)` be the ordered
tuples of `ell` distinct configurations through `v`.  Define

\[
 A_{\ell,v}={1\over(d(v))_\ell}
 \sum_{(F_1,\ldots,F_\ell)\in\mathcal T_{\ell,v}}
 \left|\bigcup_{i=1}^\ell\Gamma(F_i)\right|,         \tag{4.1}
\]

and the conditional union exposure

\[
                         U_{\ell,v}=A_{\ell,v}-d(v).  \tag{4.2}
\]

The subtraction is forced because the entire star of `v` lies in every
`Gamma(F_i)` and is already excluded by conditioning on survival of `v`.

### Theorem 4.1 (fixed factorial order)

For every fixed `ell` and `p Delta_C<=1/4`,

\[
 \boxed{
 {\mathbb E[(d_{H_p}(v))_\ell\mid v\text{ survives}]
       \over(d(v))_\ell}
 =1-pU_{\ell,v}+O_\ell(p^2\Delta_C^2).}              \tag{4.3}
\]

#### Proof

The falling factorial `(d_(H_p)(v))_ell` counts ordered distinct
`ell`-tuples through `v` which all survive.  Apply Lemma 3.1 to each tuple,
sum, and divide by `(d(v))_ell`.  This gives

\[
 {\mathbb E(d_{H_p}(v))_\ell\over(d(v))_\ell}
 =1-pA_{\ell,v}+O_\ell(p^2\Delta_C^2).                \tag{4.4}
\]

Divide by (3.9).  Since `A_(ell,v)<=ell Delta_C`, the error remains
`O_ell(p^2 Delta_C^2)`, and (4.3) follows.
\(\square\)

Thus a direct sixth-moment transfer through a microbite requires the
rooted profiles `U_(ell,v)` for `1<=ell<=6`.  This is a finite local
hierarchy, but it is not encoded by the maximum/average degree cap.

### Corollary 4.2 (six aggregate exposure sums suffice for the purge moment)

For one shore define, for `1<=ell<=6`,

\[
 F_{\ell,\sigma}=\sum_{v\in V_\sigma}(d(v))_\ell,     \tag{4.5}
\]

\[
 G_{\ell,\sigma}=
 \sum_{v\in V_\sigma}
 \sum_{(F_1,\ldots,F_\ell)\in\mathcal T_{\ell,v}}
 \left|\bigcup_{i=1}^\ell\Gamma(F_i)\right|.         \tag{4.6}
\]

Then

\[
 \boxed{
 \mathbb E F_{\ell,\sigma}(H_p)
 =F_{\ell,\sigma}(H)-pG_{\ell,\sigma}(H)
   +O_\ell(p^2\Delta_C^2F_{\ell,\sigma}(H)).}         \tag{4.7}
\]

For order zero put

\[
 F_{0,\sigma}=|V_\sigma|,qquad G_{0,\sigma}=k_\sigma Z. \tag{4.8}
\]

Then

\[
 \mathbb EF_{0,\sigma}(H_p)
 =F_{0,\sigma}(H)-pG_{0,\sigma}(H)
   +O(p^2\Delta_CG_{0,\sigma}(H)).                   \tag{4.9}
\]

Consequently, when the center is the deterministic moving annealed average
`a(p)=bar d_sigma^ann(p)`, the first-order evolution of the expected
aggregate sixth centered degree mass on the shore is determined by the
seven scalars `G_(ell,sigma)`, `0<=ell<=6`, together with the current
falling-factorial sums.

#### Proof

Sum (4.4), before conditioning on survival of `v`, over all targets of the
shore.  This gives (4.7).  Equation (4.9) is (3.12) before normalization.

For completeness, let `S(j,ell)` be the Stirling number of the second kind
and define

\[
 c_\ell(a)=\sum_{j=\ell}^6{6\choose j}
                   (-a)^{6-j}S(j,\ell).              \tag{4.10}
\]

The identities

\[
 d^j=\sum_{\ell=0}^jS(j,\ell)(d)_\ell,
 \qquad
 \sum_{v\in V_\sigma}(d(v)-a)^6
 =\sum_{\ell=0}^6c_\ell(a)F_{\ell,\sigma}           \tag{4.11}
\]

are just the binomial theorem and the standard falling-factorial expansion;
the latter follows by counting functions from a `j`-set according to the
partition into nonempty inverse images.  Substituting (4.7)--(4.9) in
(4.11), taking `a=a(p)=bar d_sigma^ann(p)`, and differentiating the explicit
coefficients proves the last assertion.  This statement does not replace
the annealed center by the random realized post-bite average; doing that
requires a separate edge-count concentration input.
\(\square\)

Thus the annealed first-order part of the stopped aggregate purge does not
require pointwise control of every `U_(ell,v)`.  A possible proof may instead
track the six aggregate union-exposure sums (4.6), together with the shore
size, edge count, and the already separate concentration of the realized
average around its annealed value.

## 5. Companion-degree and duplicate-excess form

For an edge `F`, define its duplicate excess

\[
 \mathfrak E(F)=\sum_{G:G\cap F\ne\varnothing}(|G\cap F|-1).  \tag{5.1}
\]

Double-counting incidences gives

\[
 C_F=\sum_{u\in F}d(u)-\mathfrak E(F).              \tag{5.2}
\]

Consequently the first rooted exposure can be written exactly as

\[
 \boxed{
 E_v={1\over d(v)}\sum_{F\ni v}
       \left(\sum_{u\in F-\{v\}}d(u)-\mathfrak E(F)\right).}  \tag{5.3}
\]

This displays the two missing pieces directly: companion-degree mass and
duplicate-conflict mass around a Palm root.

There is also an exact incidence average.  Let
`S_(2,sigma)=sum_(v in V_sigma)d(v)^2`.  Then

\[
 {1\over k_\sigma Z}\sum_{v\in V_\sigma}d(v)E_v
 =\overline C-{S_{2,\sigma}\over k_\sigma Z},        \tag{5.4}
\]

and therefore

\[
 {1\over k_\sigma Z}\sum_{v\in V_\sigma}d(v)\Xi_v
 =\bar d_\sigma-{S_{2,\sigma}\over k_\sigma Z}\le0. \tag{5.5}
\]

#### Proof

Using (1.4) and summing first over incident pairs `(v,F)`,

\[
 \sum_{v\in V_\sigma}d(v)E_v
 =\sum_F\sum_{v\in F\cap V_\sigma}(C_F-d(v))
 =k_\sigma Z\overline C-S_{2,\sigma}.               \tag{5.6}
\]

This proves (5.4); subtract the incidence average of
`overline C-bar d_sigma` to get (5.5).  The last inequality is Cauchy:
`S_(2,sigma)>=|V_sigma|bar d_sigma^2=k_sigma Z bar d_sigma`.
\(\square\)

## 6. A perfect cap does not control exposure

Let `H_F` be the Fano-plane triple system: seven vertices and seven
3-edges, every vertex has degree three, and every two edges intersect.
Let `H_K` be the complete 3-uniform hypergraph on four vertices: four
edges, every vertex has degree three, and every two edges intersect.  Let

\[
                         H=H_F\ \dot\cup\ H_K.       \tag{6.1}
\]

Every one of the eleven vertices has degree three, so

\[
                         \Delta(H)/\bar d(H)=1.       \tag{6.2}
\]

Nevertheless, a Fano edge has `C_F=7`, while a complete-four edge has
`C_F=4`.  Hence

\[
                         \overline C={7\cdot7+4\cdot4\over11}
                                     ={65\over11}.    \tag{6.3}
\]

For a Fano target and a complete-four target, respectively,

\[
 E_v=7-3=4,\qquad E_v=4-3=1,                         \tag{6.4}
\]

so (1.5) gives

\[
                         \Xi_v={12\over11},qquad
                         \Xi_v=-{21\over11}.          \tag{6.5}
\]

Thus the two target classes have opposite normalized conditional drifts
despite the perfect degree cap.

There is also a finite one-bite cap failure.  On the event that exactly one
Fano edge and no complete-four edge is marked, which has probability

\[
                         7p(1-p)^{10}>0,              \tag{6.6}
\]

that Fano edge is accepted.  It meets every Fano edge, so the residual has
only the four complete-four edges.  Three Fano vertices were deleted and
the other four remain with degree zero.  Thus the residual has eight
vertices, four edges, average degree

\[
                         {3\cdot4\over8}={3\over2},    \tag{6.7}
\]

and maximum degree three.  Its maximum/average ratio is exactly two.

This example does not occur as a claimed punctured residual.  Its role is
precise: it disproves every proposed conditional cap-preservation theorem
whose hypotheses contain only uniformity, current average degree, and a
maximum/average cap.

## 7. Exact remaining punctured statement

For the full punctured configuration hypergraph, edge transitivity makes
`C_F` constant and each target shore is transitive.  Hence `Xi_v=0`
initially within each shore.  The obstruction is created, if at all, by the
adaptive residual shape.

A direct fixed-root microbite proof of Gate A must therefore show, under the
stopped actual law, that the rooted union-exposure profiles in
(4.1)--(4.3) retain the concentration needed for the sixth centered degree
moment.  At first order the minimal statistic is the stopped Palm lower
tail of `Xi_v`; at orders two through six it is the corresponding finite
family `U_(ell,v)`.  For the aggregate purge actually used by Gate A,
Corollary 4.2 compresses this further to the six scalar sums
`G_(ell,sigma)`, together with the edge and shore counts.  The fixed-slice
theorem supplies the desired values under a uniform slice, but neither
exchangeability of shore labels nor the degree cap alone transfers these
profiles to the adaptive law.

This is strictly narrower than comparing complete residual states and
strictly stronger than tracking degrees alone.  No assertion here closes
that remaining profile comparison.
