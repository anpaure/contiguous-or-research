# The punctured isolated-edge nibble has a first-order cluster drift

**Date:** 2026-08-21  
**Status:** exact infinitesimal audit and corrected conditional gate; no
quenched concentration theorem or near-perfect matching is claimed

## 1. The infinitesimal isolated-edge nibble

Let `H` be a finite simple hypergraph.  Independently mark every edge with
probability `p`, retain a marked edge exactly when no other marked edge
meets it, and delete all vertices of the retained edges.  For an edge `e`
and a vertex `v`, write

\[
 s_e(p)=\Pr(e\text{ has no deleted vertex}),\qquad
 s_v(p)=\Pr(v\text{ is not deleted}).                  \tag{1.1}
\]

Let

\[
 \Gamma(e)=\{F:F\cap e\ne\varnothing\},qquad
 t_F(e)=|F\cap e|,
\]

and define the duplicate excess

\[
 \mathfrak E(e)
   =\sum_{F:t_F(e)>0}(t_F(e)-1)
   =\sum_{v\in e}d(v)-|\Gamma(e)|.                    \tag{1.2}
\]

### Proposition 1.1 (exact first derivative)

For every edge `e`,

\[
 \boxed{\qquad
 {d\over dp}\log {s_e(p)\over\prod_{v\in e}s_v(p)}
       \bigg|_{p=0}=\mathfrak E(e).
 \qquad}                                               \tag{1.3}
\]

#### Proof

At `p=0`, all survival probabilities equal one.  To first order, exactly
one edge is marked, and a single marked edge is automatically isolated.
Consequently

\[
 s_e'(0)=-|\Gamma(e)|,
 \qquad
 s_v'(0)=-d(v).                                       \tag{1.4}
\]

Taking the logarithmic derivative of (1.1) and using (1.2) proves (1.3).
`square`

The identity is unaffected by how slowly the bite is subdivided.  Slowing
the bite reduces both the target-density motion and the cluster correction
by the same factor.

## 2. The drift constant in the punctured configuration hypergraph

Now take `H=\mathcal C_r`, the directed punctured-configuration
hypergraph, and fix a configuration `e`.  Put

\[
 S(e)=\sum_F {t_F(e)\choose2},
 \qquad
 M_3(e)=\sum_F {t_F(e)\choose3}.                       \tag{2.1}
\]

For every integer `t>=0`,

\[
 0\le {t\choose2}-(t-1)\mathbf1_{t>0}
      ={(t-1)(t-2)\over2}\mathbf1_{t\ge3}
      \le {t\choose3}.                                \tag{2.2}
\]

Therefore

\[
                         0\le S(e)-\mathfrak E(e)\le M_3(e).   \tag{2.3}
\]

The third moment needed here follows directly from the frozen
boundary-codegree theorem.  Indeed,

\[
 M_3(e)=\sum_{T\in{e\choose3}}\deg(T).                 \tag{2.4}
\]

Classify the three boundary edges of `T` by their number of connected
components, and write `q=|V(B(T))|`.  In the bounded-degree boundary graph
there are `O(r)` connected triples; triangle-freeness for `b>=11` gives
`q>=4`.  There are
`O(r^2)` triples consisting of a connected two-edge path and an isolated
edge, for which `q=5`, and `O(r^3)` triples of isolated edges, for which
`q=6`.  The boundary-codegree inequality therefore gives

\[
 {M_3(e)\over D_M}
 \le C^3\left(O(r)r^{-2}+O(r^2)r^{-3}+O(r^3)r^{-4}\right)
 =O(r^{-1}).                                           \tag{2.5}
\]

The finitely many `b<11` are absorbed by the constant.  Together with the
exact pair-profile theorem, this gives

\[
 {S(e)\over D_M}=12+O(r^{-1}),
 \qquad {M_3(e)\over D_M}=O(r^{-1}).                   \tag{2.6}
\]

Combining (2.3) and (2.6) yields the exact scale

\[
 \boxed{\qquad
             {\mathfrak E(e)\over D_M}=12+O(r^{-1}).
 \qquad}                                               \tag{2.7}
\]

For a microbite with

\[
                         p={\delta\over rD_M},          \tag{2.8}
\]

equation (1.3) says that the logarithmic edge-survival correction relative
to product target survival has initial derivative

\[
                         {12+O(r^{-1})\over r}\,d\delta.       \tag{2.9}
\]

A middle target's logarithmic survival decrement is `d delta/r` to first
order; a lower target's is `(1+2/r)d delta/r`.  Thus (2.9) is on the same
`1/r` scale as the density motion itself, not on a lower-order scale.

## 3. Consequence for the proposed product-degree trajectory

Independent two-layer thinning predicts, at lower and middle residual
densities `x,y`, the middle degree

\[
                         d_x=D_Mx^{2r}y^{2r-1}.          \tag{3.1}
\]

Proposition 1.1 shows that this product manifold is not tangent-invariant
under the isolated-edge nibble.  Already at the initial symmetric state,
the derivative of edge survival differs from the product of its target
marginals by the nonzero quantity (2.7).

Equivalently, let `Z` be the number of surviving configurations.  At the
initial transitive state,

\[
 {\mathbb E Z(p)\over |E(\mathcal C_r)|}=s_e(p),        \tag{3.2}
\]

whereas the product-density prediction is the product of the `2r` lower
and `2r` middle target survival probabilities.  Their logarithmic
derivatives differ by `12D_M+O(D_M/r)`.

This does not by itself prove that a later correction cannot cancel the
drift.  It does prove that a trajectory proof cannot treat (3.1) as a
zero-drift martingale target.  A compensator, or a common empirical degree
scale which absorbs the compensator, is necessary.  Heuristically, holding
the initial coefficient fixed would produce an `x^{-12}` enrichment; that
heuristic is not used as a theorem here.

## 4. A corrected sufficient gate

After `j` bites, let `H_j` be the residual hypergraph, let `Z_j=|E(H_j)|`,
and let `M_j,L_j` be its two residual target shores.  Define the empirical
average degrees

\[
 \bar d_j^M={2rZ_j\over |M_j|},
 \qquad
 \bar d_j^L={2rZ_j\over |L_j|}.                         \tag{4.1}
\]

Every selected configuration removes exactly `2r` vertices from each
shore.  Hence, if `x_j` is the lower residual density, the middle density
is exactly

\[
                         y_j={rx_j+2\over r+2},          \tag{4.2}
\]

and

\[
 {\bar d_j^L\over\bar d_j^M}
 ={ |M_j|\over |L_j|}
 =1+{2\over r x_j}=1+o(1)                              \tag{4.3}
\]

uniformly for `x_j>=r^{-alpha}` with fixed `alpha<1`.

The following renormalized gate is sufficient for the usual bite
calculation.

> **Renormalized quenched gate `RQG(alpha)`.**  Uniformly through all rounds
> with `x_j>=r^{-alpha}`:
>
> 1. every surviving target has degree
>    `(1+o(1))\bar d_j^M` or `(1+o(1))\bar d_j^L`, according to its shore;
> 2. every surviving configuration `e` satisfies
>    \[
>             \mathfrak E_j(e)=o(r\bar d_j^M);          \tag{4.4}
>    \]
> 3. the empirical scale does not collapse exponentially relative to the
>    product prediction:
>    \[
>      \log\bar d_j^M
>       \ge \log\!\left(D_Mx_j^{2r}y_j^{2r-1}\right)
>             -o(r\log r);                              \tag{4.5}
>    \]
> 4. when configurations are marked with `p_j` from (4.7), if `A_j` is the
>    number of isolated marked edges retained in round `j`, then,
>    simultaneously over the trajectory,
>    \[
>      A_j=(1+o(1))\mathbb E(A_j\mid H_j)
>          =(1+o(1))Z_jp_j e^{-4\gamma}.                \tag{4.6}
>    \]

### Proposition 4.1 (the renormalized gate is enough)

For any fixed `alpha<1/2`, `RQG(alpha)` implies a matching leaving
`r^{-alpha}+o(1)` of the lower shore and `o(1)` of the middle shore.

#### Proof

In round `j`, mark each surviving configuration with

\[
                         p_j={\gamma\over r\bar d_j^M}   \tag{4.7}
\]

for a fixed sufficiently small positive `gamma`.  By (4.1), (4.3), and
uniform degree regularity, for every surviving edge `e`,

\[
 \sum_{v\in e}d_j(v)-\mathfrak E_j(e)
          =(4+o(1))r\bar d_j^M.                         \tag{4.8}
\]

Thus a marked edge is isolated with probability
`exp(-4gamma+o(1))`.  Put `lambda=gamma exp(-4gamma)`.  By (4.1),
(4.3), and Assumption 4, the fractions of the residual lower and middle
shores covered in round `j` are respectively

\[
 {2rA_j\over |L_j|}
   ={\bar d_j^L\over\bar d_j^M}{\lambda+o(1)\over r}
   ={\lambda+o(1)\over r},
 \qquad
 {2rA_j\over |M_j|}={\lambda+o(1)\over r}.             \tag{4.9}
\]

Consequently

\[
 x_{j+1}=x_j\left(1-{\lambda+o(1)\over r}\right)       \tag{4.10}
\]

uniformly over the trajectory.  The first round with
`x_j<=r^{-alpha}` occurs after

\[
 J=\left({\alpha\over\lambda}+o(1)\right)r\log r
   =\left({\alpha e^{4\gamma}\over\gamma}+o(1)\right)r\log r
   =O(r\log r/\gamma).                                  \tag{4.11}
\]

The one-round overshoot is a multiplicative `1+O(1/r)`, so the stopping
density is `r^{-alpha}(1+O(1/r))`.

At that density,

\[
 \log\!\left(D_Mx_j^{2r}y_j^{2r-1}\right)
      =(2-4\alpha+o(1))r\log r.                         \tag{4.12}
\]

Equations (4.5) and (4.12) keep the empirical degree exponential for
`alpha<1/2`, so the process does not run out of configurations before the
stopping density.  The exact shore relation (4.2) gives the claimed leave.
`square`

## 5. Scope and the remaining concentration problem

The boundary-codegree theorem and its polymer summation prove, for an
independent residual and fixed `alpha<1/3`,

\[
 {\mathbb E\mathfrak E_x(e)\over r d_x}
       =O\!\left({1\over r x^3}\right)=o(1).            \tag{5.1}
\]

The corresponding possible compensator scale satisfies

\[
 \int_x^1 O(u^{-3})\,d\log(1/u)=O(x^{-3}).              \tag{5.2}
\]

At `x=r^{-alpha}`, `alpha<1/3`, this is `o(r log r)`, consistent with the
weaker exponential lower bound (4.5).  Equation (5.2) is a scale check,
not a quenched trajectory proof.

What remains is to prove uniform concentration around the empirical
scales in `RQG(alpha)`.  There are `exp(Theta(r))` targets but

\[
                         (2r+1)!=\exp((2+o(1))r\log r)  \tag{5.3}
\]

configurations.  A direct union bound therefore needs failure probability
`exp(-omega(r))` for each target-degree variable and at most
`exp(-(2+omega(1))r log r)` for each edge-indexed duplicate variable.
The polynomial number of rounds is negligible at these scales.

The proved boundary-codegree gate is a one-root overlap estimate.  A
quenched martingale proof must additionally control connected multi-root
overlap cumulants after conditioning on the nibble history.  No such
uniform cumulant or trajectory theorem is asserted here.

In particular, the first-order drift does **not** obstruct a near-perfect
matching.  It only retires the unnecessarily rigid requirement that the
actual nibble degrees remain `(1+o(1))` times the independent-product value
throughout the trajectory.
